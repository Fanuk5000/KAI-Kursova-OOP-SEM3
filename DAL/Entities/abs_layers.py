from abc import ABC, abstractmethod
from multiprocessing.util import abstract_sockets_supported

class ABCFootballPlayer(ABC):  
    @abstractmethod  
    def __str__(self) -> str: # type: ignore
        pass

    @abstractmethod
    def to_dict(self) -> dict: # type: ignore
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> 'FootballPlayer': # type: ignore
        pass

class ABCFootballMatch(ABC):

    @abstractmethod
    def add_player(self, player: 'FootballPlayer') -> None: # type: ignore
        pass
    
    @abstractmethod
    def remove_player(self, player_id: str) -> None:
        pass
    
    @abstractmethod
    def to_dict(self) -> dict: # type: ignore
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> 'FootballMatch': # type: ignore
        pass

    @abstractmethod
    def __str__(self) -> str: # type: ignore
        pass


class ABCFootballStadium(ABC):
    @abstractmethod
    def to_dict(self) -> dict: # type: ignore
        pass
    
    @abstractmethod
    @classmethod
    def from_dict(cls, data: dict) -> 'FootballStadium': # type: ignore
        pass

    @abstractmethod
    def __str__(self) -> str: # type: ignore
        pass
