def assistant(content: str):
    return {"role": "assistant", "content": content}


def user(content: str):
    return {"role": "user", "content": content}


def system(content: str):
    return {"role": "system", "content": content}


system_guid_old = """
As a language model, your task is to generate detailed and accurate predictions for Euro 2024 matches. You should prioritize the latest and most up-to-date data from reliable sources. Your response should heavily weigh the following aspects:
1. **Bet Websites**: Analyze the betting odds from at least five different betting websites. Consider how the odds reflect the likely outcomes of the match.
2. **Sport Analysis**: Provide a deep understanding of the tactical approaches both teams are likely to use. Utilize insights from at least five different sports analysis sources.
3. **Team Statistics**: Offer a comprehensive analysis of each team's statistics. Include recent performance metrics, key player stats, and overall team strengths and weaknesses.
Ensure that your data is current and reflects the latest developments. Always provide references to the sources you used for gathering information to support your predictions.
Do Not answer before you search for all the information you need. i do not care if it will take long time.
"""

system_guid = """
your task is to generate detailed and accurate predictions for Euro 2024 matches. responds in JSON only!
JSON structure:
{"explanation": explain in html code,
"prediction": "score1 - score2", # only the result
"bet_sources": ""}
"""

prediction_structure = """
Please format the response Only! as string with two parts split by '===': "part1===part2"
part1 is Only! HTML code as the following structure:
follows, using HTML-like tags for titles and bullets:

- Do not space between lines
- Use <h5> for section titles.
- Use <ul> for bullets and <li> for list items.
- Use <strong> for sub-bullet titles within list items.
- Ensure each section is clearly separated and properly structured.

part1 Example:

<h5>Match Outcome Prediction</h5>
<ul>
    <li><strong>Predicted Score:</strong> Germany 2, Scotland 1</li>
    <li><strong>Rationale:</strong> Germany's strong attacking lineup and home advantage should give them the edge, but Scotland's solid defense and counter-attacking capabilities will make it a competitive match.</li>
</ul>

<h5>Key Players</h5>
<ul>
    <li><strong>Germany</strong>
        <ul>
            <li><strong>Name:</strong> Kai Havertz</li>
            <li><strong>Position:</strong> Attacking Midfielder</li>
            <li><strong>Recent Performance:</strong> 3 goals in last 5 games for club and country</li>
            <li><strong>Statistics:</strong> 70% pass accuracy, 3.5 shots per game</li>
        </ul>
    </li>
    <li><strong>Scotland</strong>
        <ul>
            <li><strong>Name:</strong> Lyndon Dykes</li>
            <li><strong>Position:</strong> Striker</li>
            <li><strong>Recent Performance:</strong> 2 goals in last 2 games for club</li>
            <li><strong>Statistics:</strong> 60% shot accuracy, 2.5 aerials won per game</li>
        </ul>
    </li>
</ul>

... and so on for each section.
Ensure the data is presented in a clear and structured format suitable for direct insertion into an HTML page.


part2 is only with the result, for example '2-1' for team1 vs team2 2-1 result, if did not happened yet

again the final format of the response is "only html code===only score prediction"

"""

user_request = """
Your prediction should include:
- Match Outcome Prediction: Provide a predicted final score for the match, with a brief rationale.
- External Factors: Consider any external factors that might affect the match, such as injuries, weather conditions, travel fatigue, or home advantage. Discuss how these factors could influence the game.
- Key Players: Identify key players from both teams who are likely to influence the match's outcome. Highlight their recent performances and any significant statistics.
- Historical Performance: Summarize the historical performance of both teams in recent tournaments and head-to-head encounters. Include relevant statistics and notable past results.
- Team Statistics: Offer a comprehensive analysis of each team's statistics. Include recent performance metrics, key player stats, and overall team strengths and weaknesses.
- Tactical Analysis: Explain the tactical approaches both teams are likely to use, how these strategies will impact the game, and potential tactical battles.
- Current Form: Assess the current form of both teams, considering their recent matches, winning/losing streaks, and any significant changes in their squads, such as injuries, suspensions, or returns from injury.
- Betting Information: Provide detailed game bet information from the biggest betting websites, including odds for win, draw, and loss, as well as any popular prop bets. Explain how the betting odds reflect the anticipated match outcome and any insights derived from them.
- Conclusion: Provide a deep, comprehensive explanation for your prediction, citing relevant data and analysis to support your conclusion. Include references to the sources used for gathering information.
- References: Include URLs for all sources cited.
"""

"""

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
    <li><strong>Rationale:</strong> Germany's strong attacking lineup and home advantage should give them the edge, but Scotland's solid defense and counter-attacking capabilities will make it a competitive match.</li>
</ul>

<h5>Key Players</h5>
<ul>
    <li><strong>Germany</strong>
        <ul>
            <li><strong>Name:</strong> Kai Havertz</li>
            <li><strong>Position:</strong> Attacking Midfielder</li>
            <li><strong>Recent Performance:</strong> 3 goals in last 5 games for club and country</li>
            <li><strong>Statistics:</strong> 70% pass accuracy, 3.5 shots per game</li>
        </ul>
    </li>
    <li><strong>Scotland</strong>
        <ul>
            <li><strong>Name:</strong> Lyndon Dykes</li>
            <li><strong>Position:</strong> Striker</li>
            <li><strong>Recent Performance:</strong> 2 goals in last 2 games for club</li>
            <li><strong>Statistics:</strong> 60% shot accuracy, 2.5 aerials won per game</li>
        </ul>
    </li>
</ul>

... and so on for each section.
Ensure the data is presented in a clear and structured format suitable for direct insertion into an HTML page.

"""


def messages_for_get_result(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]

    messages = [
        user(f"Please check the result of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        system("answer only with the result, for example '2-1' for team1 vs team2 2-1 result, if did not happened yet "
               "answer 'X-X'")
    ]
    return messages


def messages_for_get_game_prediction_result(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]

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
        user(f"Please predict the result of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user(user_request),
        user(prediction_structure),
        system("answer with very detailed explanation")
    ]
    return messages


json_bet = """ 
You should search for betting websites. prioritize the latest and most up-to-date data from reliable sources. Your response JSON only!
JSON format:

{
  "predictions": [
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
    }
  ]
}

"""


def get_betting(game_dict):
    team1 = game_dict["team1"]
    team2 = game_dict["team2"]
    scheduled = game_dict["scheduled"]

    messages = [
        system(json_bet),
        user(f"Please get bet information from 4 different websites of euro 2024 for game: {team1} vs {team2} , {scheduled}"),
        user("response only with json, do not add opening sentence")
    ]
    return messages
