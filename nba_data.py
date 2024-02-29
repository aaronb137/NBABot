from operator import itemgetter
from nba_api.live.nba.endpoints import scoreboard

"""
TODO: Retrieve teams and their score !DONE
TODO: Retrieve game leaders and their stats !DONE
"""


def get_latest_games():
    """Retrieve and return today's games."""
    return scoreboard.ScoreBoard().games.get_dict()


def is_winner_status(game):
    """Calculate the winner status based on scores."""
    return int(game["homeTeam"]["score"]) > int(game["awayTeam"]["score"])


def is_game_over(game):
    """Check if the game is over."""
    if not isinstance(game["gameStatusText"], str):
        raise ValueError("Not str value")

    return game["gameStatusText"] == "Final"


def get_teams(game):
    """Get the names of the away and home teams."""
    homeTeamName, awayTeamName = (
        game["homeTeam"]["teamName"],
        game["awayTeam"]["teamName"],
    )

    # Check if either team values are empty
    if (homeTeamName == "") or (awayTeamName == ""):
        raise ValueError("Str value empty")

    return awayTeamName, homeTeamName


def get_game_scores(game):
    """Get the scores of the away and home teams."""
    return int(game["awayTeam"]["score"]), int(game["homeTeam"]["score"])


def get_game_leaders(game):
    """Get the leaders of the away and home teams."""
    if not isinstance(game, dict):
        raise TypeError("Invalid type; expected dict")

    return game["gameLeaders"]["awayLeaders"], game["gameLeaders"]["homeLeaders"]


def parse_game_leader(leader):
    """Parses JSON for game leader stats"""

    # Check for correct type
    if not isinstance(leader, dict):
        raise TypeError("Invalid type; expected dict")

    leader_keys = [
        "name",
        "jerseyNum",
        "position",
        "teamTricode",
        "points",
        "rebounds",
        "assists",
    ]
    leader_values = itemgetter(*leader_keys)(leader)
    leader_dict = dict(zip(leader_keys, leader_values))
    return leader_dict


def get_game(team, games_par=None):
    """Get the game information for a given team."""
    if games_par is not None:
        games = games_par
    else:
        games = get_latest_games()

    # Parses list of games until the provided team is found inside the list then return a game dict
    for game in games:
        if (
            game["awayTeam"]["teamName"].lower() == team.lower()
            or game["homeTeam"]["teamName"].lower() == team.lower()
        ):
            return game

    print(f"Cannot find game for {team.title()}")
    return None
