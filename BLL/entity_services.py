# here will be edited configuration of football matches and players
from os import path

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

from DAL.file_manipulations import PlayerFileManager, MatchFileManager

class PlayerService:
    def __init__(self):
        self.player_file_manager = PlayerFileManager("football_players.json")
        
    def add_player_to_file(self, new_player: FootballPlayer) -> None:
        if not isinstance(new_player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        players = self.player_file_manager.deserialize()
        players.append(new_player)
        self.player_file_manager.serialize(players)
    
    def del_player_from_file(self, player_id: str) -> None:
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string while deleting player from file")
        players = self.player_file_manager.deserialize()
        suitable_players = [player for player in players if player.id == player_id]
        
        if suitable_players:
            for player in suitable_players:
                players.remove(player)
            self.player_file_manager.serialize(players)
        else:
            print(f"No player with id {player_id} found")
    
    # possible attributes to change: name, surname, birth_date, status, health, salary
    def change_player_attribute(self, player_id: str, attribute: str, new_value) -> None:
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string")

        players = self.player_file_manager.deserialize()
        suitable_players = [player for player in players if player.id == player_id]

        if suitable_players:
            for player in suitable_players:
                if not hasattr(player, attribute):
                    raise AttributeError(f"Player does not have an attribute '{attribute}'")
                try:
                    setattr(player, attribute, new_value)
                except TypeError as e:
                    print(f"TypeError occurred while change_player_attribute '{attribute}': {e}")
                except ValueError as e:
                    print(f"ValueError occurred while change_player_attribute '{attribute}': {e}")
            self.player_file_manager.serialize(players)
        else:
            print(f"No player with id {player_id} found")

class MatchService:
    def __init__(self):
        self.match_file_manager = MatchFileManager("football_mathces.json")
        self.player_file_manager = PlayerFileManager("football_players.json")

    def add_match_to_file(self, new_match: FootballMatch) -> None:
        if not isinstance(new_match, FootballMatch):
            raise TypeError("Expected a FootBallMatch instance")
        matches = self.match_file_manager.deserialize()
        matches.append(new_match)
        self.match_file_manager.serialize(matches)
    
    def del_match_from_file(self, match_id: str):
        pass
    
    def add_player_to_match(self, chosen_match_id: str, new_player: FootballPlayer) -> None:
        if not isinstance(chosen_match_id, str):
            raise TypeError("match_id must be a string while adding player to the match")
        if not isinstance(new_player, FootballPlayer):
            raise TypeError("new_player must be a FootballPlayer class while adding to the match")
        
        players = self.player_file_manager.deserialize()
        if new_player not in players:
            raise ValueError("Player must be added to the players list before being added to a match")
        
        matches = self.match_file_manager.deserialize()
        suitable_matches:list[FootballMatch] = [match for match in matches if match.id == chosen_match_id]
        
        if suitable_matches:
            for match in suitable_matches:
                match.add_player(new_player)
        else:
            print(f"No match with id {chosen_match_id} found")
    
    def del_player_from_match(self, chosen_match_id: str, player_id: str) -> None:
        if not isinstance(chosen_match_id, str):
            raise TypeError("match_id must be a string while deleting player from the match")
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string while deleting player from the match")

        matches = self.match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == chosen_match_id]
    
        if suitable_matches:
            for match in suitable_matches:
                try:
                    match.remove_player(player_id)
                except ValueError as e:
                    print(f"No such player with id {player_id} found in match {chosen_match_id}: {e}")
        else:
            print(f"No match with id {chosen_match_id} found")
    
    def change_match_attribute(self, match_id: str, attribute: str, new_value) -> None:
        if not isinstance(match_id, str):
            raise TypeError("match_id must be a string")
        
        matches = self.match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == match_id]

        if suitable_matches:
            for match in suitable_matches:
                try:
                    setattr(match, attribute, new_value)
                except AttributeError as e:
                    print(f"AttributeError occurred while change_match_attribute '{attribute}': {e}")
                except TypeError as e:
                    print(f"TypeError occurred while change_match_attribute '{attribute}': {e}")
                except ValueError as e:
                    print(f"ValueError occurred while change_match_attribute '{attribute}': {e}")
        else:
            print(f"No match with id {match_id} found")

class StadiumService:
    def __init__(self):
        pass