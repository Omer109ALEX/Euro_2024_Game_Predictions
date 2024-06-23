def calculate_probabilities(team1_win_points, team2_win_points, draw_points, game_odds, strike_points):
    probabilities = {}
    for score, odds in game_odds.items():
        if score.count('-') != 1:
            continue

        team1_score, team2_score = map(int, score.split('-'))

        if team1_score > team2_score:
            points = team1_win_points
        elif team1_score < team2_score:
            points = team2_win_points
        else:
            points = draw_points

        points = points + strike_points

        try:
            probabilities[score] = {
                "percentage": odds,
                "points": str(float(odds) * points)
            }
        except ValueError:
            probabilities[score] = {
                "percentage": odds,
                "points": "Invalid odds value"
            }
    return probabilities


def get_top_5_scores(data):
    # Convert points from strings to floats for comparison
    scores = {score: float(details['points']) for score, details in data.items()}

    # Sort the scores dictionary by points in descending order and get the top 5
    top_5 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]

    # Print the top 5 scores
    print("Top 5 scores by points:")
    for score, points in top_5:
        print(f"Score: {score}, Points: {points}")

    return top_5


# Example usage

"""
    "1-0": ,
    "2-0": ,
    "3-0": ,
    "2-1": ,
    "3-1": ,
    "0-0": ,
    "1-1": ,
    "2-2": ,
    "0-1": ,
    "0-2": ,
    "0-3": ,
    "1-2": ,
    "1-3": ,
"""
game_odds = {
    "1-0": 10,
    "2-0": 15,
    "3-0": 5,
    "2-1": 20,
    "3-1": 10,
    "0-0": 10,
    "1-1": 15,
    "2-2": 10,
    "0-1": 5,
    "0-2": 5,
    "0-3": 2,
    "1-2": 5,
    "1-3": 3
}

team1_win_points = 2.5
draw_points = 3
team2_win_points = 3.5
strike_points = 4

probabilities = calculate_probabilities(team1_win_points, team2_win_points, draw_points, game_odds, strike_points)
print(probabilities)

# Call the function with the example input
top_5 = get_top_5_scores(probabilities)
