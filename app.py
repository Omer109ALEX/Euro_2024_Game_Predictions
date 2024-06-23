from flask import Flask, render_template,send_from_directory, request, jsonify, make_response
import json
import use_llm as llm
import create_messages as cm
import requests
from datetime import datetime




#local_run = http://127.0.0.1:5000/
app = Flask(__name__)

PASSWORD = "omer"
NEXT_GAME_ID = 22

# Function to load predictions from a JSON file
def load_predictions(filename="games.json"):
    with open(filename, 'r') as f:
        return json.load(f)

# Function to save predictions to a JSON file
def save_predictions_to_file(predictions, filename="games.json"):
    with open(filename, 'w') as f:
        json.dump(predictions, f, indent=4)


# Load predictions at startup
predictions = load_predictions()


@app.route('/refresh_betting_info', methods=['GET'])
def refresh_betting_info():
    game_id = request.args.get('game_id')
    password = request.args.get('password')

    if not password:
        return jsonify({'message': 'password parameter is required'}), 400

    if password != PASSWORD:
        return jsonify({'message': 'Invalid password'}), 403

    game = next((item for item in predictions if item["id"] == game_id), None)
    if game:
        messages = cm.get_betting(game)
        string_result = llm.chat_completion(messages)
        betting_websites = game["betting_websites"]
        result_list = json.loads(string_result)
        if isinstance(betting_websites, str):
            betting_websites = json.loads(betting_websites)
        for bet in result_list:
            betting_websites.append(bet)
        game["betting_websites"] = betting_websites # Update the betting_websites in the game dictionary
        save_predictions_to_file(predictions)  # Save updated predictions to file
        return make_response("", 204)  # No Content
    return jsonify({"error": "Game not found"}), 404

@app.route('/')
def index():
    return render_template('index.html', predictions=predictions)

@app.route('/game/<string:game_id>')
def game_details(game_id):
    game = next((item for item in predictions if item["id"] == game_id), None)
    return render_template('game.html', game=game, game_id=game_id)

@app.route('/load_game')
def load_game():
    return render_template('load_game.html')


@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/flags.json')
def flags():
    return send_from_directory('', 'flags.json')

@app.route('/games.json')
def games():
    return send_from_directory('', 'games.json')


def get_final_score(team1, team2, date_and_time):
    # Load the JSON data from the URL
    url = "https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json"
    response = requests.get(url)
    data = json.loads(response.text)

    # Convert the string to a datetime object
    datetime_obj = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M")
    date_str = datetime_obj.strftime("%Y-%m-%d")

    if team1 == 'Czechia':
        team1 = 'Czech Republic'
    if team2 == 'Czechia':
        team2 = 'Czech Republic'

    for round in data.get('rounds', []):
        for match in round.get('matches', []):
            if (match['team1']['name'] == team1 and match['team2']['name'] == team2 and match['date'] == date_str) or \
                    (match['team1']['name'] == team2 and match['team2']['name'] == team1 and match['date'] == date_str):
                score1 = match.get('score', {}).get('ft', [None, None])[0]
                score2 = match.get('score', {}).get('ft', [None, None])[1]
                if score1 is not None and score2 is not None:
                    return f"{score1}-{score2}"
                else:
                    return "X-X"
    return "Match not found"


@app.route('/get_result', methods=['POST'])
def get_result():
    game_id = request.json.get('game_id')
    game = next((item for item in predictions if item["id"] == game_id), None)
    if game:
        team1 = game["team1"]
        team2 = game["team2"]
        scheduled = game["scheduled"]
        final_score = get_final_score(team1, team2, scheduled)
        game["result"] = final_score  # Update the result in the game dictionary
        save_predictions_to_file(predictions)  # Save updated predictions to file
        return jsonify({"result": final_score})
    return jsonify({"error": "Game not found"}), 404

@app.route('/get_game_prediction', methods=['POST'])
def get_game_prediction():
    game_id = request.json.get('game_id')
    game = next((item for item in predictions if item["id"] == game_id), None)
    if game:
        answer = llm.chat_completion(cm.messages_for_get_game_prediction_explanation(game))
        #answer = llm.chat_completion(cm.predict_by_bet(game))

        answer_list = answer.split("===")
        explanation = answer_list[0]
        prediction = answer_list[1]
        game["prediction"] = prediction  # Update the prediction in the game dictionary
        game["prediction_explanation"] = explanation  # Update the explanation in the game dictionary
        save_predictions_to_file(predictions)  # Save updated predictions to file
        return jsonify({"prediction": prediction, "explanation": explanation})
    return jsonify({"error": "Game not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
