import json


def update_points_by_id(id_to_update, team1_points, team2_points, draw_points, file_path="games.json"):
    # Load the existing games.json file
    with open(file_path, "r") as file:
        games = json.load(file)

    for game in games:
        if game['id'] == id_to_update:
            game['points']['team1'] = team1_points
            game['points']['team2'] = team2_points
            game['points']['draw'] = draw_points

            # Optionally, update result explanation or any other fields if needed
            game['result_explanation'] = f"Points updated for {game['team1']} vs {game['team2']}"

            break

    # Save the updated games.json file
    with open(file_path, "w") as file:
        json.dump(games, file, indent=4)


def update_games_file(add_fields=None, update_fields=None, remove_fields=None, clear_fields=None, file_path="games.json"):
    """
    Update the games.json file by adding, updating, removing, or clearing fields.

    Parameters:
    - file_path (str): The path to the games.json file.
    - add_fields (dict): Fields to add with their default values.
    - update_fields (dict): Fields to update with their new values.
    - remove_fields (list): List of fields to remove.
    - clear_fields (list): List of fields to clear (set to empty string).

    Example usage:
    - add_fields = {'new_field': 'default_value'}
    - update_fields = {'status': 'scheduled'}
    - remove_fields = ['old_field']
    - clear_fields = ['description']
    """
    # Load the existing games.json file
    with open(file_path, "r") as file:
        games = json.load(file)

    # Add new fields
    if add_fields:
        for game in games:
            for field, value in add_fields.items():
                game[field] = value

    # Update existing fields
    if update_fields:
        for game in games:
            for field, value in update_fields.items():
                if field in game:
                    game[field] = value

    # Remove specified fields
    if remove_fields:
        for game in games:
            for field in remove_fields:
                if field in game:
                    del game[field]

    # Clear specified fields
    if clear_fields:
        for game in games:
            for field in clear_fields:
                if field in game:
                    game[field] = ""

    # Save the updated games.json file
    with open(file_path, "w") as file:
        json.dump(games, file, indent=4)

    print(f"Updated games entries in {file_path}")

# Example usage:
add_fields = {'sport_5_id': ""}
#update_fields = {'status': 'scheduled'}
#remove_fields = ['points']
#clear_fields = ['description']

update_games_file(add_fields=add_fields)
games = [
    {
        "id": "34",
        "round": "Round of 16",
        "team1": "Germany",
        "team2": "Denmark",
        "scheduled": "2024-06-29 20:00",
    },
    {
        "id": "35",
        "round": "Round of 16",
        "team1": "Switzerland",
        "team2": "Italy",
        "scheduled": "2024-06-29 17:00",
    },
    {
        "id": "36",
        "round": "Round of 16",
        "team1": "Spain",
        "team2": "Georgia",
        "scheduled": "2024-06-30 20:00",
    },
    {
        "id": "37",
        "round": "Round of 16",
        "team1": "England",
        "team2": "Slovakia",
        "scheduled": "2024-06-30 17:00",
    },
    {
        "id": "38",
        "round": "Round of 16",
        "team1": "Portugal",
        "team2": "Slovenia",
        "scheduled": "2024-07-01 20:00",
    },
    {
        "id": "39",
        "round": "Round of 16",
        "team1": "France",
        "team2": "Belgium",
        "scheduled": "2024-07-01 17:00",
    },
    {
        "id": "40",
        "round": "Round of 16",
        "team1": "Romania",
        "team2": "Netherlands",
        "scheduled": "2024-07-02 18:00",
    },
    {
        "id": "41",
        "round": "Round of 16",
        "team1": "Austria",
        "team2": "Turkey",
        "scheduled": "2024-07-02 21:00",
    },
    {
        "id": "42",
        "round": "Quarterfinals",
        "team1": "Winner Match 39",
        "team2": "Winner Match 37",
        "scheduled": "2024-07-05 18:00",
    },
    {
        "id": "43",
        "round": "Quarterfinals",
        "team1": "Winner Match 41",
        "team2": "Winner Match 42",
        "scheduled": "2024-07-05 21:00",
    },
    {
        "id": "44",
        "round": "Quarterfinals",
        "team1": "Winner Match 43",
        "team2": "Winner Match 44",
        "scheduled": "2024-07-06 18:00",
    },
    {
        "id": "45",
        "round": "Quarterfinals",
        "team1": "Winner Match 40",
        "team2": "Winner Match 38",
        "scheduled": "2024-07-06 21:00",
    },
    {
        "id": "46",
        "round": "Semifinals",
        "team1": "Winner Match 45",
        "team2": "Winner Match 46",
        "scheduled": "2024-07-09 21:00",
    },
    {
        "id": "47",
        "round": "Semifinals",
        "team1": "Winner Match 47",
        "team2": "Winner Match 48",
        "scheduled": "2024-07-10 21:00",
    },
    {
        "id": "48",
        "round": "Final",
        "team1": "Winner Semifinal 1",
        "team2": "Winner Semifinal 2",
        "scheduled": "2024-07-14 21:00",
    }
]
