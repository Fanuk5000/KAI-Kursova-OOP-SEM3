from abc import ABC, abstractmethod
from DAL.Entities.football_mathces import FootBallMatch
from DAL.Entities.football_player import FootballPlayer

class ABCPlayerFileManager(ABC):
    @abstractmethod
    def serialize(self, ft_players: list[FootballPlayer]) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list[FootballPlayer] | None:
        pass

class ABCMatchFileManager(ABC):
    @abstractmethod
    def serialize(self, matches: list[FootBallMatch]) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list[FootBallMatch] | None:
        pass