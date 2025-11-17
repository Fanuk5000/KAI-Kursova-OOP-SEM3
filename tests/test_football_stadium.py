import pytest
from uuid import uuid4

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

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
def setup_working_football_stadium(setup_working_football_match):
    football_stadium = FootballStadium(
        stadium_name="Stadium A",   
        seats_amount=50000,
        price_for_place=50.0,
        football_match=setup_working_football_match
    )
    yield football_stadium

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
        viewers=1000,
        id=pre_generated_id
    )
    yield football_match

def test_football_stadium_initialization(setup_working_football_stadium, setup_working_football_match):
    football_stadium = setup_working_football_stadium

    assert football_stadium.stadium_name == "Stadium A"
    assert football_stadium.seats_amount == 50000
    assert football_stadium.price_for_place == 50.0
    assert football_stadium.football_match == setup_working_football_match
    assert football_stadium.id == pre_generated_id

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