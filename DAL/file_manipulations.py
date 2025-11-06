from os import path
import json
from DAL.Entities.football_mathces import FootBallMatch
from DAL.abstract_filemanager import ABCPlayerFileManager, ABCMatchFileManager
from DAL.Entities.football_player import FootballPlayer


# Players and Matches will be in separate files
class PlayerFileManager(ABCPlayerFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, ft_players: list[FootballPlayer]) -> None:
        try:
            couple_players = [player.to_dict() for player in ft_players]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_players, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing: {e}")

    def deserialize(self) -> list[FootballPlayer] | list:
        try:
            if not path.exists(self.__filename):
                return []
            with open(self.__filename, "r", encoding="utf-8") as file:
                players_dicts = json.load(file)
            return [FootballPlayer.from_dict(player_dict) for player_dict in players_dicts]
        except IOError as e:
            print(f"I/O error: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error while deserializing: {e}")
            return []


class MatchFileManager(ABCMatchFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, matches: list[FootBallMatch]) -> None:
        try:
            couple_matches = [match.to_dict() for match in matches]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_matches, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing: {e}")

    def deserialize(self) -> list[FootBallMatch] | list:
        try:
            if not path.exists(self.__filename):
                return []
            with open(self.__filename, "r", encoding="utf-8") as file:
                matches_dicts = json.load(file)
            return [FootBallMatch.from_dict(match_dict) for match_dict in matches_dicts]
        except IOError as e:
            print(f"I/O error: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error while deserializing: {e}")
            return []