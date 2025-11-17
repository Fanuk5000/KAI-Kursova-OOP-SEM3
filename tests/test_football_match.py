from uuid import uuid4

import pytest

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer



@pytest.fixture()
def setup_working_football_player():
    global pre_generated_id
    pre_generated_id = str(uuid4())
    football_player = FootballPlayer(
        name="John",
        surname="Doe",
        birth_date="15-08-1990",
        status="active",
        health=95.5,
        salary=50000.0,
        id=pre_generated_id
    )
    yield football_player

@pytest.fixture()
def setup_working_football_match(setup_working_football_player):
    football_match = FootballMatch(
        match_place="Stadium A",
        home_team="Team A",
        away_team="Team B",
        match_date="20-09-2023",
        match_status="not_played_yet",
        score="00:00",
        players=[setup_working_football_player],
        viewers=1000
    )
    yield football_match

def test_football_match_initialization(setup_working_football_match, setup_working_football_player):
    football_match = setup_working_football_match

    assert football_match.match_place == "Stadium A"
    assert football_match.home_team == "Team A"
    assert football_match.away_team == "Team B"
    assert football_match.match_date == "20-09-2023"
    assert football_match.match_status == "not_played_yet"
    assert football_match.score == "00:00"
    assert football_match.players == [setup_working_football_player]
    assert football_match.viewers == 1000
    assert football_match.id == pre_generated_id

def test_football_match_invalid_match_place(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(TypeError):
        football_match.match_place = 123  # type: ignore

def test_football_match_invalid_home_team(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(TypeError):
        football_match.home_team = 123  # type: ignore

def test_football_match_invalid_away_team(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(TypeError):
        football_match.away_team = 456  # type: ignore

def test_football_match_invalid_match_date(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(ValueError):
        football_match.match_date = "2023/09-20"  # Incorrect format

    with pytest.raises(ValueError):
        football_match.match_date = "20_09_2023"  # type: ignore

    with pytest.raises(TypeError):
        football_match.match_date = 20230920  # type: ignore

def test_football_match_invalid_match_status(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(TypeError):
        football_match.match_status = 789  # type: ignore
    
    with pytest.raises(ValueError):
        football_match.match_status = "Bro"

def test_football_match_invalid_score(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(ValueError):
        football_match.score = "5-3"  # Incorrect format

    with pytest.raises(ValueError):
        football_match.score = "Five:Three"  # type: ignore

    with pytest.raises(TypeError):
        football_match.score = 53  # type: ignore

def test_football_match_invalid_players(setup_working_football_match, setup_working_football_player):
    football_match = setup_working_football_match
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_match.players = ["NotAPlayer"]  # type: ignore
    
    with pytest.raises(TypeError):
        football_match.players = [football_player, "NotAPlayer"]  # type: ignore

def test_football_match_add_remove_player(setup_working_football_match, setup_working_football_player):
    football_match = setup_working_football_match
    football_player = setup_working_football_player
    my_id = str(uuid4())

    new_player = FootballPlayer(
        name="Alice",
        surname="Smith",
        birth_date="22-11-1992",
        status="active",
        health=90.0,
        salary=60000.0,
        id=my_id
    )

    football_match.add_player(new_player)
    assert new_player in football_match.players

    with pytest.raises(ValueError):
        football_match.add_player(new_player)  # Adding the same player again

    football_match.remove_player(new_player.id)
    assert new_player not in football_match.players

    with pytest.raises(ValueError):
        football_match.remove_player("NonExistentID")

def test_football_match_invalid_viewers(setup_working_football_match):
    football_match = setup_working_football_match

    with pytest.raises(TypeError):
        football_match.viewers = "Many"  # type: ignore

    with pytest.raises(ValueError):
        football_match.viewers = -100

    with pytest.raises(ValueError):
        football_match.viewers = 0