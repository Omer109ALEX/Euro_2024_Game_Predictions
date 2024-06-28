import json

def assistant(content: str):
    return {"role": "assistant", "content": content}


def user(content: str):
    return {"role": "user", "content": content}


def system(content: str):
    return {"role": "system", "content": content}


system_guid = """
As a language model, your task is to generate detailed and accurate predictions for Euro 2024 matches.
You should prioritize the data from reliable sources. the latest update is always better.
Ensure that your data is current and reflects the latest developments.
Always provide references to the sources you used for gathering information to support your predictions.
Do Not answer before you search for all the information you need. i do not care if it will take long time.
"""

system_guid_not_good = """
your task is to generate detailed and accurate predictions for Euro 2024 matches. responds in JSON only!
JSON structure:
{"explanation": explain in html code,
"prediction": "score1 - score2", # only the result
"bet_sources": ""}
"""

prediction_structure = """
Please format the response as string with two parts split by '===': "part1===part2"
do not add any more tokens.
part2 is only score with no text, for example "2-1"
part1 is Only! HTML code with format:

html_format:
follows, using HTML-like tags for titles and bullets:

- Do not space between lines
- Use <h5> for section titles.
- Use <ul> for bullets and <li> for list items.
- Use <strong> for sub-bullet titles within list items.
- Ensure each section is clearly separated and properly structured.

<h5>Match Outcome Prediction</h5>
<ul>
    <li><strong>Predicted Score:</strong> Germany 2, Scotland 1</li>
</ul>

<h5>Betting odds</h5>
<ul>
    <li><strong>score</strong>
        <ul>
  
... and so on for each section.
Ensure the data is presented in a clear and structured format suitable for direct insertion into an HTML page.

"""

user_request = """
Your prediction should include:
- Match Outcome Prediction: Provide a predicted final score for the match, with a brief rationale.
- Recent Performance: use data only from: https://www.uefa.com/euro2024/fixtures-results , explain about last matches from euro 2024 tournament 
- External Factors: Consider any external factors that might affect the match, such as injuries, home advantage. Discuss how these factors could influence the game.
- Key Players: Identify key players from both teams who are likely to influence the match's outcome. Highlight their recent performances and any significant statistics.
- Historical Performance: Summarize the historical performance of both teams in recent tournaments and head-to-head encounters. Include relevant statistics and notable past results.
- Team Statistics: Offer a comprehensive analysis of each team's statistics. Include recent performance metrics, key player stats, and overall team strengths and weaknesses.
- Tactical Analysis: Explain the tactical approaches both teams are likely to use, how these strategies will impact the game, and potential tactical battles.
- Current Form: Assess the current form of both teams, considering their recent matches, winning/losing streaks, and any significant changes in their squads, such as injuries, suspensions, or returns from injury.
- Betting Information: Provide detailed game bet information from the biggest betting websites, including odds for win, draw, and loss from same website, as well as any popular prop bets. Explain how the betting odds reflect the anticipated match outcome and any insights derived from them.
- Conclusion: Provide a deep, comprehensive explanation for your prediction, citing relevant data and analysis to support your conclusion. Include references to the sources used for gathering information.
- References: Include URLs for all sources cited.
"""


def messages_for_get_game_prediction_result(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]
    round = game_dict["round"]

    messages = [
        system(system_guid),
        user(f"Please predict the result of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user(user_request),
        user("Provide answer with only the result in the format 'score - score' do not add any more words")
    ]
    return messages


def test(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]

    messages = [
        system(system_guid),
        user(f"Please predict the result of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user(user_request),
    ]
    return messages


def messages_for_get_game_prediction_explanation(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]

    messages = [
        system(system_guid),
        system(f'today is the {scheduled}, give your answer based on today date'),
        user(f"Please predict the result of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user(user_request),
        user(prediction_structure),
        system("answer with very detailed explanation")
    ]
    return messages


json_bet = """ 
You should search for betting websites. prioritize the latest and most up-to-date data from reliable sources. Your response JSON only!
JSON format:

[
  {
    "website_name": "",
    "website_url": "",
    "betting_options": {
      "match_result": {
        "team1_win": "",
        "draw": "",
        "team2_win": ""
      },
      "double_chance": {
        "team1_or_draw": "",
        "team2_or_draw": "",
        "team1_or_team2": ""
      },
      "over_under_goals": {
        "over_2_5_goals": "",
        "under_2_5_goals": ""
      },
      "both_teams_to_score": {
        "yes": "",
        "no": ""
      },
      "correct_score": {
        "team1_score_team2_score": ""
      },
      "total_goals_by_team": {
        "team1_over_1_5_goals": "",
        "team1_under_1_5_goals": "",
        "team2_over_1_5_goals": "",
        "team2_under_1_5_goals": ""
      },
      "winning_margin": {
        "team1_by_1_goal": "",
        "team1_by_2_goals": "",
        "team1_by_3_or_more_goals": "",
        "team2_by_1_goal": "",
        "team2_by_2_goals": "",
        "team2_by_3_or_more_goals": ""
      },
      "handicap_betting": {
        "team1_handicap_1": "",
        "team2_handicap_1": ""
      },
      "draw_no_bet": {
        "team1_win": "",
        "team2_win": ""
      }
    }
  },
  {
    "website_name": "",
    "website_url": "",
    "betting_options": {
      "match_result": {
        "team1_win": "",
        "draw": "",
        "team2_win": ""
      },
      "double_chance": {
        "team1_or_draw": "",
        "team2_or_draw": "",
        "team1_or_team2": ""
      },
      #more and more
    }
  }
]

"""


def get_betting(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]
    """
    betting_websites = game_dict["betting_websites"]
    if isinstance(betting_websites, str):
        betting_websites = json.loads(betting_websites)
    current_website_names_list = [site['website_name'] for site in betting_websites]
    """

    messages = [
        system(json_bet),
        user(
            f"Please get new bet information from 4 websites, different than of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user("response only with json, do not add opening sentence")
    ]
    return messages


def predict_by_bet(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]
    current_betting_websites = game_dict["betting_websites"]

    messages = [
        user(f"Please predict and explain the score result for game: {team1} vs {team2},based on average info from all this data: {current_betting_websites} "),
        user(prediction_structure),
    ]
    return messages
