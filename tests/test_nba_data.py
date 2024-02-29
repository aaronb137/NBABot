import pytest
import nba_data as nba

"""
* Coverage so far (8 functions):
*   -> test return latest games (1 funct)
*   -> test winner home/away (1 funct)
*   -> test game over invalid/valid (1 funct)
*   -> test valid game leaders type (1 funct)
*   -> test get teams invalid/valid (1 funct)
*   -> test get team scores invalid/valid (1 funct)
*   -> test parse team leader valid/invalid (1 funct)
*   -> test game retrieval valid/invalid (1 funct)

* 8/8 functions tested
"""


def test_latest_games_returns_list() -> None:
    """Tests if function returns list of games"""
    games = nba.get_latest_games()
    assert isinstance(games, list)


def test_is_winner_home() -> None:
    """Tests for proper return for home team win"""
    game = {"homeTeam": {"score": 125}, "awayTeam": {"score": 100}}
    assert nba.is_winner_status(game) == 1, "Home team should be winner"


def test_is_winner_away() -> None:
    """Tests for proper return for away team win"""
    game = {"homeTeam": {"score": 100}, "awayTeam": {"score": 125}}
    assert nba.is_winner_status(game) == 0, "Away team should be winner"


def test_if_game_is_over_invalid() -> None:
    """Tests for handling of invalid types for is_game_over"""
    game = {"gameStatusText": 5}

    with pytest.raises(ValueError):
        nba.is_game_over(game)


def test_if_game_is_over_valid() -> None:
    """Tests for handling of invalid types for is_game_over"""
    game = {"gameStatusText": "Final"}

    nba.is_game_over(game)


def test_get_game_leaders_valid_type() -> None:
    """Tests for happy case when retrieving game leaders"""
    game = {
        "gameLeaders": {
            "homeLeaders": {
                "personId": 203083,
                "name": "Andre Drummond",
                "jerseyNum": "3",
                "position": "C",
                "teamTricode": "CLE",
                "playerSlug": "None",
                "points": 33,
                "rebounds": 23,
                "assists": 3,
            },
            "awayLeaders": {
                "personId": 203944,
                "name": "Julius Randle",
                "jerseyNum": "30",
                "position": "F-C",
                "teamTricode": "NYK",
                "playerSlug": "None",
                "points": 28,
                "rebounds": 6,
                "assists": 6,
            },
        }
    }

    nba.get_game_leaders(game)


def test_get_game_leaders_invalid_type() -> None:
    """Tests for invalid case when retrieving game leaders"""
    game = 5

    with pytest.raises(TypeError):
        nba.get_game_leaders(game)


def test_get_teams() -> None:
    game = {
        "gameId": "0022000181",
        "gameCode": "20210115/NYKCLE",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-01-16T00:30:00Z",
        "gameEt": "2021-01-15T19:30:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
            "teamId": 1610612739,
            "teamName": "Cavaliers",
            "teamCity": "Cleveland",
            "teamTricode": "CLE",
            "wins": 6,
            "losses": 7,
            "score": 106,
            "inBonus": "None",
            "timeoutsRemaining": 1,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 28}],
        },
        "awayTeam": {
            "teamId": 1610612752,
            "teamName": "Knicks",
            "teamCity": "New York",
            "teamTricode": "NYK",
            "wins": 5,
            "losses": 8,
            "score": 103,
            "inBonus": "None",
            "timeoutsRemaining": 0,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 25}],
        },
    }

    nba.get_teams(game)


def test_get_teams_invalid() -> None:
    game = {
        "gameId": "0022000181",
        "gameCode": "20210115/NYKCLE",
        "gameStatus": 3,
        "gameStatusText": "Final",
        "period": 4,
        "gameClock": "",
        "gameTimeUTC": "2021-01-16T00:30:00Z",
        "gameEt": "2021-01-15T19:30:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
            "teamId": 1610612739,
            "teamName": "",
            "teamCity": "Cleveland",
            "teamTricode": "CLE",
            "wins": 6,
            "losses": 7,
            "score": 106,
            "inBonus": "None",
            "timeoutsRemaining": 1,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 28}],
        },
        "awayTeam": {
            "teamId": 1610612752,
            "teamName": "",
            "teamCity": "New York",
            "teamTricode": "NYK",
            "wins": 5,
            "losses": 8,
            "score": 103,
            "inBonus": "None",
            "timeoutsRemaining": 0,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 25}],
        },
    }

    with pytest.raises(ValueError):
        nba.get_teams(game)


def test_get_game_scores() -> None:
    """Testing happy case for getting game scores"""
    game = {
        "homeTeam": {
            "score": 0,
        },
        "awayTeam": {
            "score": 0,
        },
    }

    nba.get_game_scores(game)


def test_get_game_scores_invalid() -> None:
    game = {
        "homeTeam": {
            "score": "",
        },
        "awayTeam": {
            "score": "chicken",
        },
    }

    with pytest.raises(ValueError):
        nba.get_game_scores(game)


def test_leader_parsing_valid() -> None:
    """Test happy case for leader parsing"""
    leader = {
        "personId": 203944,
        "name": "Julius Randle",
        "jerseyNum": "30",
        "position": "F-C",
        "teamTricode": "NYK",
        "playerSlug": "None",
        "points": 28,
        "rebounds": 6,
        "assists": 6,
    }

    nba.parse_game_leader(leader)


def test_leader_parsing_invalid() -> None:
    """Test unhappy case when invalid type for leader parsing"""
    leader = 10

    with pytest.raises(TypeError):
        nba.parse_game_leader(leader)


def test_leader_parsing_invalid_key() -> None:
    """Test unhappy case when dict is missing key for leader parsing"""
    leader = {
        "personId": 203944,
        "jerseyNum": "30",
        "position": "F-C",
        "teamTricode": "NYK",
        "playerSlug": "None",
        "points": 28,
        "rebounds": 6,
        "assists": 6,
    }

    with pytest.raises(KeyError):
        nba.parse_game_leader(leader)


def test_get_game_valid() -> None:
    """Test happy case for finding game"""
    games = [
        {
            "gameId": "0022300768",
            "homeTeam": {
                "teamName": "Mavericks",
            },
            "awayTeam": {
                "teamName": "Wizards",
            },
        },
        {
            "gameId": "0022300770",
            "homeTeam": {
                "teamName": "Clippers",
            },
            "awayTeam": {
                "teamName": "Timberwolves",
            },
        },
    ]

    result = nba.get_game("Clippers", games)
    assert result is not None


def test_get_game_invalid():
    games = [
        {
            "gameId": "0022300768",
            "homeTeam": {
                "teamName": "Mavericks",
            },
            "awayTeam": {
                "teamName": "Wizards",
            },
        },
        {
            "gameId": "0022300770",
            "homeTeam": {
                "teamName": "Nuggets",
            },
            "awayTeam": {
                "teamName": "Timberwolves",
            },
        },
    ]

    result = nba.get_game("Clippers", games)
    assert result is None
