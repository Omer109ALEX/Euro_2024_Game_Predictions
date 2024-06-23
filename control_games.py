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
#add_fields = {'points': {"team1": 0,"team2": 0,"draw": 0}}
#update_fields = {'status': 'scheduled'}
#remove_fields = ['new_field']
#clear_fields = ['description']

#update_games_file(add_fields, update_fields, remove_fields, clear_fields)

to_update = [
    {
        "round": "Group Stage, Round 1",
        "team1": "Germany",
        "team2": "Scotland",
        "scheduled": "2024-06-14 22:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Hungary",
        "team2": "Switzerland",
        "scheduled": "2024-06-15 16:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Spain",
        "team2": "Croatia",
        "scheduled": "2024-06-15 19:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Italy",
        "team2": "Albania",
        "scheduled": "2024-06-15 22:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Poland",
        "team2": "Netherlands",
        "scheduled": "2024-06-16 16:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Slovenia",
        "team2": "Denmark",
        "scheduled": "2024-06-16 19:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Serbia",
        "team2": "England",
        "scheduled": "2024-06-16 22:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Romania",
        "team2": "Ukraine",
        "scheduled": "2024-06-17 19:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Belgium",
        "team2": "Slovakia",
        "scheduled": "2024-06-17 22:00"
    },
    {
        "round": "Group Stage, Round 1",
        "team1": "Austria",
        "team2": "France",
        "scheduled": "2024-06-17 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Germany",
        "team2": "Hungary",
        "scheduled": "2024-06-19 19:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Scotland",
        "team2": "Switzerland",
        "scheduled": "2024-06-19 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Slovenia",
        "team2": "Serbia",
        "scheduled": "2024-06-20 19:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Denmark",
        "team2": "England",
        "scheduled": "2024-06-20 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Spain",
        "team2": "Italy",
        "scheduled": "2024-06-20 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Poland",
        "team2": "Austria",
        "scheduled": "2024-06-21 19:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Netherlands",
        "team2": "France",
        "scheduled": "2024-06-21 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Slovakia",
        "team2": "Ukraine",
        "scheduled": "2024-06-22 16:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Belgium",
        "team2": "Romania",
        "scheduled": "2024-06-22 22:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Georgia",
        "team2": "Czechia",
        "scheduled": "2024-06-22 16:00"
    },
    {
        "round": "Group Stage, Round 2",
        "team1": "Türkiye",
        "team2": "Portugal",
        "scheduled": "2024-06-22 19:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Switzerland",
        "team2": "Germany",
        "scheduled": "2024-06-23 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Scotland",
        "team2": "Hungary",
        "scheduled": "2024-06-23 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Croatia",
        "team2": "Italy",
        "scheduled": "2024-06-24 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Albania",
        "team2": "Spain",
        "scheduled": "2024-06-24 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Netherlands",
        "team2": "Austria",
        "scheduled": "2024-06-25 19:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "France",
        "team2": "Poland",
        "scheduled": "2024-06-25 19:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Denmark",
        "team2": "Serbia",
        "scheduled": "2024-06-25 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "England",
        "team2": "Slovenia",
        "scheduled": "2024-06-25 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Slovakia",
        "team2": "Romania",
        "scheduled": "2024-06-26 19:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Ukraine",
        "team2": "Belgium",
        "scheduled": "2024-06-26 19:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Czechia",
        "team2": "Türkiye",
        "scheduled": "2024-06-26 22:00"
    },
    {
        "round": "Group Stage, Round 3",
        "team1": "Georgia",
        "team2": "Portugal",
        "scheduled": "2024-06-26 22:00"
    }
]

