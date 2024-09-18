
# Euro 2024 Game Predictions

This project is a web application that provides predictions for Euro 2024 football matches. The application displays match predictions, key players, tactical analysis, historical performance, current form, external factors, betting information, and a detailed explanation for each prediction.

## Features

- Displays match predictions for Euro 2024 games
- Provides detailed analysis including key players, tactics, and historical performance
- Integrates with betting websites for odds and insights
- User-friendly interface with match details and predictions

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

## Installation

You need to add the Groq API key.

1. Clone the repository:

   ```sh
   git clone https://github.com/Omer109ALEX/Euro_2024_Game_Predictions.git
   cd euro2024-predictions
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set the Flask environment variables:
   ```sh
   set FLASK_APP=app.py  # On Windows
   export FLASK_APP=app.py  # On macOS/Linux
   ```
   

5. Run the application:
   ```sh
   flask run
   ```

6. Open your web browser and navigate to http://127.0.0.1:5000 to view the application.
Here you can see my web for example: https://euro-2024-game-predictions.onrender.com/

```
