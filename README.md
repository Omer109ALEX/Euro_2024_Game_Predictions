
# Euro 2024 Game Predictions

This project is a web application that provides predictions for Euro 2024 football matches. The application displays match predictions, key players, tactical analysis, historical performance, current form, external factors, betting information, and a detailed explanation for each prediction.

![image](https://github.com/user-attachments/assets/be806a07-0485-42ab-a156-b0fde09bc444)

## Features

- Displays match predictions for Euro 2024 games
- Provides detailed analysis including key players, tactics, and historical performance
- Integrates with betting websites for odds and insights
- User-friendly interface with match details and predictions

![image](https://github.com/user-attachments/assets/f6abfa54-406e-4d53-b787-5398e13250c7)


![image](https://github.com/user-attachments/assets/534be19a-b3c2-4be6-96c9-f3c5f9bc2892)


## Project Structure

```sh
├── 109
│   └── # contains guesses data from Sport 5 from 109 group
├── templates
│   ├── index.html
│   ├── game.html
│   └── load_game.html
├── top
│   └── # contains guesses data from Sport 5 from top group
├── README.md
├── app.py
├── create_messages.py
├── flags.json
├── game_format.json
├── games.json
├── requirements.txt
├── spot_5.py
├── use_llm.py
```

- `app.py`: Main application file that contains the Flask routes and logic.
- `create_messages.py`: Contains functions to create messages and insights for LLM.
- `flags.json`: JSON file for game flags data.
- `game_format.json`: JSON file for game format details.
- `games.json`: JSON file containing the scheduled games and predictions.
- `spot_5.py`: Script for collecting data from the Sport 5 website about game guesses.
- `use_llm.py`: Integration with the LLM for generating insights.
- `templates/`: Directory containing HTML templates for the web pages.
- `requirements.txt`: List of Python dependencies.

