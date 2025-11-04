import json
from DAL.abstract_filemanager import ABCFileManager
from DAL.Entities.football_player import FootballPlayer


# Players and Matches will be in separate files
class PlayerFileManager(ABCFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, ft_players: list[FootballPlayer]) -> None:
        try:
            print(ft_players.__dict__)
            couple_players: list = [ft_player.__dict__ for ft_player in ft_players]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_players, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing: {e}")

    def deserialize(self) -> list[FootballPlayer] | None:
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                players_dicts = json.load(file)
            return [FootballPlayer(**player_dict) for player_dict in players_dicts]
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        except Exception as e:
            print(f"An unexpected error while deserializing: {e}")


class MatchFileManager(ABCFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, matches: list) -> None:
        try:
            couple_matches: list = [match.__dict__ for match in matches]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(couple_matches, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        except Exception as e:
            print(f"An unexpected error while serializing: {e}")

    def deserialize(self) -> list | None:
        pass  # Implementation for matches deserialization