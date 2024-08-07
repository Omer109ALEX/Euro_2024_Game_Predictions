# Euro 2024 Game Predictions

This project is a web application that provides predictions for Euro 2024 football matches. The application displays match predictions, key players, tactical analysis, historical performance, current form, external factors, betting information, and a detailed explanation for each prediction.

## Features

- Displays match predictions for Euro 2024 games
- Provides detailed analysis including key players, tactics, and historical performance
- Integrates with betting websites for odds and insights
- User-friendly interface with match details and predictions

## Project Structure
   ```sh

├── app.py
├── create_messages.py
├── games.json
├── templates
│ ├── index.html
│ ├── game.html
│ └── load_game.html
├── static
│ ├── styles.css
│ └── scripts.js
├── requirements.txt
└── Procfile
```

- `app.py`: Main application file that contains the Flask routes and logic.
- `create_messages.py`: Contains functions to create messages for LLM.
- `games.json`: JSON file containing the scheduled games and predictions.
- `templates/`: Directory containing HTML templates for the web pages.
- `static/`: Directory for static files such as CSS and JavaScript.
- `requirements.txt`: List of Python dependencies.
- `Procfile`: Configuration file for Heroku deployment.

## Installation

need to add groq api key

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/euro2024-predictions.git
   cd euro2024-predictions

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt

4.Set the Flask environment variables:
   ```sh
   set FLASK_APP=app.py  # On Windows
   export FLASK_APP=app.py  # On macOS/Linux
  ```

5.Run the application:
   ```sh
   flask run
  ```

6.  Open your web browser and navigate to http://127.0.0.1:5000 to view the application.



