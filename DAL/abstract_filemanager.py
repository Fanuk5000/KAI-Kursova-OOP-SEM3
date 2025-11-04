from abc import ABC, abstractmethod
from DAL.Entities.football_mathes import FootBallMatch
from DAL.Entities.football_player import FootballPlayer

class PlayerFileManager(ABC):
    @abstractmethod
    def serialize(self, players: list[FootballPlayer]) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list[FootballPlayer] | None:
        pass

class MatchFileManager(ABC):
    @abstractmethod
    def serialize(self, matches: list[FootBallMatch]) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list[FootBallMatch] | None:
        pass