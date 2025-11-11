import pytest

from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_stadium import FootballStadium

@pytest.fixture()
def setup_working_football_player():
    football_player = FootballPlayer(
        name="John",
        surname="Doe",
        birth_date="15-08-1990",
        status="Active",
        health=95.5,
        salary=50000.0
    )
    yield football_player

@pytest.fixture()
def setup_working_football_match(setup_working_football_player):
    football_match = FootballMatch(
        match_place="Stadium A",
        home_team="Team A",
        away_team="Team B",
        match_date="20-09-2023",
        match_status="Not played yet",
        score="00:00",
        players=[setup_working_football_player],
        viewers=1000
    )
    yield football_match

@pytest.fixture()
def setup_working_football_stadium(setup_working_football_match):
    football_stadium = FootballStadium(
        stadium_name="Stadium A",   
        seats_amount=50000,
        price_for_place=50.0,
        football_match=setup_working_football_match
    )
    yield football_stadium

# -------------------------- Tests for FootballPlayer --------------------------
def test_football_player_initialization(setup_working_football_player):
    football_player = setup_working_football_player

    assert football_player.name == "John"
    assert football_player.surname == "Doe"
    assert football_player.birth_date == "15-08-1990"
    assert football_player.status == "Active"
    assert football_player.health == 95.5
    assert football_player.salary == 50000.0
    assert football_player.id == "JD15081990"

def test_football_player_invalid_name(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_player.name = 123  # type: ignore

def test_football_player_invalid_surname(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_player.surname = 456 # type: ignore

def test_football_player_invalid_birth_date(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(ValueError):
        football_player.birth_date = "1990/08-15"  # Incorrect format
        
    with pytest.raises(ValueError):
        football_player.birth_date = "12_12_1999"  # type: ignore

    with pytest.raises(TypeError):
        football_player.birth_date = 19900815  # type: ignore


def test_football_player_invalid_status(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_player.status = 789  # type: ignore
    
    with pytest.raises(ValueError):
        football_player.status = ""  # Empty status

def test_football_player_invalid_health(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_player.health = "Healthy"  # type: ignore

    with pytest.raises(TypeError):
        football_player.health = [100]  # type: ignore

def test_football_player_invalid_salary(setup_working_football_player):
    football_player = setup_working_football_player

    with pytest.raises(TypeError):
        football_player.salary = "Fifty Thousand"  # type: ignore

    with pytest.raises(ValueError):
        football_player.salary = -999

    with pytest.raises(ValueError):
        football_player.salary = 99999999

# -------------------------- Tests for FootballMatch --------------------------
def test_football_match_initialization(setup_working_football_match, setup_working_football_player):
    football_match = setup_working_football_match

    assert football_match.match_place == "Stadium A"
    assert football_match.home_team == "Team A"
    assert football_match.away_team == "Team B"
    assert football_match.match_date == "20-09-2023"
    assert football_match.match_status == "Not played yet"
    assert football_match.score == "00:00"
    assert football_match.players == [setup_working_football_player]
    assert football_match.viewers == 1000
    assert football_match.id == "TT20092023"

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

    new_player = FootballPlayer(
        name="Alice",
        surname="Smith",
        birth_date="22-11-1992",
        status="Active",
        health=90.0,
        salary=60000.0
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
# -------------------------- Tests for FootballStadium --------------------------
def test_football_stadium_initialization(setup_working_football_stadium, setup_working_football_match):
    football_stadium = setup_working_football_stadium

    assert football_stadium.stadium_name == "Stadium A"
    assert football_stadium.seats_amount == 50000
    assert football_stadium.price_for_place == 50.0
    assert football_stadium.football_match == setup_working_football_match
    assert football_stadium.id == "S5000050.0A"

def test_football_stadium_invalid_stadium_name(setup_working_football_stadium):
    football_stadium = setup_working_football_stadium

    with pytest.raises(TypeError):
        football_stadium.stadium_name = 123  # type: ignore

def test_football_stadium_invalid_seats_amount(setup_working_football_stadium):
    football_stadium = setup_working_football_stadium

    with pytest.raises(TypeError):
        football_stadium.seats_amount = "Fifty Thousand"  # type: ignore

    with pytest.raises(ValueError):
        football_stadium.seats_amount = -1000

    with pytest.raises(ValueError):
        football_stadium.seats_amount = 0

    with pytest.raises(ValueError):
        football_stadium.seats_amount = 60000  # Trying to increase seats amount

def test_football_stadium_invalid_football_match(setup_working_football_stadium):
    football_stadium = setup_working_football_stadium

    with pytest.raises(TypeError):
        football_stadium.football_match = "NotAMatch"  # type: ignore

def test_football_stadium_invalid_price_for_place(setup_working_football_stadium):
    football_stadium = setup_working_football_stadium

    with pytest.raises(TypeError):
        football_stadium.price_for_place = "Fifty"  # type: ignore

    with pytest.raises(ValueError):
        football_stadium.price_for_place = -50.0

    with pytest.raises(ValueError):
        football_stadium.price_for_place = 0.0