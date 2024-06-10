from flask import Flask, render_template, request, jsonify
import json
import use_llm as llm
import create_messages as cm

app = Flask(__name__)

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

@app.route('/get_result', methods=['POST'])
def get_result():
    game_id = request.json.get('game_id')
    game = next((item for item in predictions if item["id"] == game_id), None)
    if game:
        messages = cm.messages_for_get_result(game)
        result = llm.chat_completion(messages)
        game["result"] = result  # Update the result in the game dictionary
        save_predictions_to_file(predictions)  # Save updated predictions to file
        return jsonify({"result": result})
    return jsonify({"error": "Game not found"}), 404

@app.route('/get_game_prediction', methods=['POST'])
def get_game_prediction():
    game_id = request.json.get('game_id')
    game = next((item for item in predictions if item["id"] == game_id), None)
    if game:
        messages = cm.messages_for_get_game_prediction_explanation(game)
        answer = llm.chat_completion(messages)
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
