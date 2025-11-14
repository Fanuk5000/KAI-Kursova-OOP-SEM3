from abc import ABC, abstractmethod

class ABCFootballPlayer(ABC):    
    def __str__(self) -> str: # type: ignore
        pass

    def to_dict(self) -> dict: # type: ignore
        pass
    
    @classmethod
    def from_dict(cls, data: dict) -> 'FootballPlayer': # type: ignore
        pass

class ABCFootballMatch(ABC):

    def add_player(self, player: 'FootballPlayer') -> None: # type: ignore
        pass
    
    def remove_player(self, player_id: str) -> None:
        pass

    def to_dict(self) -> dict: # type: ignore
        pass

    @classmethod
    def from_dict(cls, data: dict) -> 'FootballMatch': # type: ignore
        pass

    def __str__(self) -> str: # type: ignore
        pass


class ABCFootballStadium(ABC):

    def to_dict(self) -> dict: # type: ignore
        pass

    @classmethod
    def from_dict(cls, data: dict) -> 'FootballStadium': # type: ignore
        pass

    def __str__(self) -> str: # type: ignore
        pass
