from uuid import uuid4
import pytest

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

def test_football_player_initialization(setup_working_football_player):
    football_player = setup_working_football_player

    assert football_player.name == "John"
    assert football_player.surname == "Doe"
    assert football_player.birth_date == "15-08-1990"
    assert football_player.status == "active"
    assert football_player.health == 95.5
    assert football_player.salary == 50000.0
    assert football_player.id == pre_generated_id

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
