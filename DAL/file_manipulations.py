from os import path
import json

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

from DAL.abstract_filemanager import ABCPlayerFileManager, ABCMatchFileManager, ABCStadiumFileManager

class PlayerFileManager(ABCPlayerFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, ft_players: list[FootballPlayer]) -> None:
        try:
            couple_players = [player.to_dict() for player in ft_players]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_players, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found while serializing FootballPlayer: {e}")
        except IOError as e:
            print(f"I/O error while serializing FootballPlayer: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing FootballPlayer: {e}")

    def deserialize(self) -> list[FootballPlayer] | list:
        try:
            if not path.exists(self.__filename):
                return []
            with open(self.__filename, "r", encoding="utf-8") as file:
                players_dicts = json.load(file)
            return [FootballPlayer.from_dict(player_dict) for player_dict in players_dicts]
        except IOError as e:
            print(f"I/O error while deserializing FootballPlayer: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error while deserializing FootballPlayer: {e}")
            return []


class MatchFileManager(ABCMatchFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, matches: list[FootballMatch]) -> None:
        try:
            couple_matches = [match.to_dict() for match in matches]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_matches, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found while serializing FootballMatch: {e}")
        except IOError as e:
            print(f"I/O error while serializing FootballMatch: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing FootballMatch: {e}")

    def deserialize(self) -> list[FootballMatch] | list:
        try:
            if not path.exists(self.__filename):
                return []
            with open(self.__filename, "r", encoding="utf-8") as file:
                matches_dicts = json.load(file)
            return [FootballMatch.from_dict(match_dict) for match_dict in matches_dicts]
        except IOError as e:
            print(f"I/O error while deserializing FootballMatch: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error while deserializing FootballMatch: {e}")
            return []

class StadiumFileManager(ABCStadiumFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, stadiums: list[FootballStadium]) -> None:
        try:
            couple_stadiums = [stadium.to_dict() for stadium in stadiums]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_stadiums, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found while serializing FootballStadium: {e}")
        except IOError as e:
            print(f"I/O error while serializing FootballStadium: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing FootballStadium: {e}")

    def deserialize(self) -> list[FootballStadium] | list:
        try:
            if not path.exists(self.__filename):
                return []
            with open(self.__filename, "r", encoding="utf-8") as file:
                stadiums_dicts = json.load(file)
            return [FootballStadium.from_dict(stadium_dict) for stadium_dict in stadiums_dicts]
        except IOError as e:
            print(f"I/O error while deserializing FootballStadium: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error while deserializing FootballStadium: {e}")
            return []