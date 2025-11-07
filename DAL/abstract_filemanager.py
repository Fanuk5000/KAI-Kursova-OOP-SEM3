from abc import ABC, abstractmethod

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

class ABCPlayerFileManager(ABC):
    @abstractmethod
    def serialize(self, ft_players: list['FootballPlayer']) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list['FootballPlayer'] | None:
        pass

class ABCMatchFileManager(ABC):
    @abstractmethod
    def serialize(self, matches: list['FootballMatch']) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list['FootballMatch'] | None:
        pass

class ABCStadiumFileManager(ABC):
    @abstractmethod
    def serialize(self, stadiums: list['FootballStadium']) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list['FootballStadium'] | None:
        pass