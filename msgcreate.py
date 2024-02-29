import io
import sys
import nba_data as nba
from timehelper import get_today_date


def print_game(game):
    output = io.StringIO()  # Create a StringIO object to capture printed output
    sys.stdout = output  # Redirect stdout to the StringIO object

    today_date = get_today_date()

    away_team, home_team = nba.get_teams(game)
    away_score, home_score = nba.get_game_scores(game)
    away_leader, home_leader = nba.get_game_leaders(game)

    aleader_stats = nba.parse_game_leader(away_leader)
    hleader_stats = nba.parse_game_leader(home_leader)

    print(f"# {today_date}")

    if nba.is_winner_status(game) == 0:
        print(f"# {away_team} won!\n\n")
    else:
        print(f"# {home_team} won!\n\n")

    print("__FINAL SCORE__")
    print(f"Away: {away_team} {away_score}\nHome: {home_team} {home_score}\n")

    print("__GAME LEADERS__")
    print("PTS REB AST\n")

    print(f"**Away Leader:** \n{aleader_stats['name']}")
    print(
        f"{aleader_stats['teamTricode']} | {aleader_stats['jerseyNum']} | {aleader_stats['position']}"
    )
    print(
        f"{aleader_stats['points']} - {aleader_stats['rebounds']} - {aleader_stats['assists']}\n"
    )

    print(f"**Home Leader:** \n{hleader_stats['name']}")
    print(
        f"{hleader_stats['teamTricode']} | {hleader_stats['jerseyNum']} | {hleader_stats['position']}"
    )
    print(
        f"{hleader_stats['points']} - {hleader_stats['rebounds']} - {hleader_stats['assists']}\n"
    )

    sys.stdout = sys.__stdout__  # Reset stdout to its original value
    return output.getvalue()  # Get the captured output as a string
