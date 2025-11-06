# here will be edited configuration of football matches and players
from os import path

from DAL.Entities.football_mathces import FootBallMatch
from DAL.Entities.football_player import FootballPlayer

from DAL.file_manipulations import PlayerFileManager, MatchFileManager

class EntityService:
    def __init__(self):
        self.player_file_manager = PlayerFileManager("football_players.json")
        self.match_file_manager = MatchFileManager("football_mathces.json")
    
    def add_player_to_file(self, new_player: FootballPlayer) -> None:
        if not isinstance(new_player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        players = self.player_file_manager.deserialize()
        players.append(new_player)
        self.player_file_manager.serialize(players)
    
    def add_match_to_file(self, new_match: FootBallMatch) -> None:
        if not isinstance(new_match, FootBallMatch):
            raise TypeError("Expected a FootBallMatch instance")
        matches = self.match_file_manager.deserialize()
        matches.append(new_match)
        self.match_file_manager.serialize(matches)
    
    def add_player_to_match(self, chosen_match_id: str, new_player: FootballPlayer):
        if not isinstance(chosen_match_id, str):
            raise TypeError("match_id must be a string while adding player to the match")
        if not isinstance(new_player, FootballPlayer):
            raise TypeError("new_player must be a FootballPlayer class while adding to the match")
        matches = self.match_file_manager.deserialize()
        suitable_matches:list[FootBallMatch] = [match for match in matches if match.id == chosen_match_id]
        
        if suitable_matches:
            for match in suitable_matches:
                match.add_player(new_player)
        else:
            raise ValueError(f"No match with id {chosen_match_id} found")