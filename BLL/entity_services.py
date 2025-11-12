from os import path

from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

from DAL.file_manipulations import PlayerFileManager, MatchFileManager, StadiumFileManager

match_file_manager = MatchFileManager("football_matches.json")
stadium_file_manager = StadiumFileManager("football_stadiums.json")
player_file_manager = PlayerFileManager("football_players.json")

class PlayerService:
    @staticmethod
    def add_player_to_file(new_player: FootballPlayer) -> None:
        if not isinstance(new_player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        players = player_file_manager.deserialize()
        players.append(new_player)
        player_file_manager.serialize(players)

    @staticmethod
    def del_player_from_file(player_id: str) -> None:
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string while deleting player from file")
        players = player_file_manager.deserialize()
        suitable_players = [player for player in players if player.id == player_id]
        
        if suitable_players:
            for player in suitable_players:
                players.remove(player)
            player_file_manager.serialize(players)
        else:
            print(f"No player with id {player_id} found")
    
    # possible attributes to change: name, surname, birth_date, status, health, salary
    @staticmethod
    def change_player_attribute(player_id: str, attribute: str, new_value) -> None:
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string")

        players = player_file_manager.deserialize()
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
            player_file_manager.serialize(players)
        else:
            print(f"No player with id {player_id} found")
    
    @staticmethod
    def player_info(player_id: str) -> None:
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string while getting player info")
        players = player_file_manager.deserialize()
        suitable_players = [player for player in players if player.id == player_id]
        
        if suitable_players:
            for player in suitable_players:
                print(player)
        else:
            print(f"No player with id {player_id} found")

    @staticmethod
    def list_all_players() -> None:
        players = player_file_manager.deserialize()
        for player in players:
            print(player)

class MatchService:
    @staticmethod
    def add_match_to_file(new_match: FootballMatch) -> None:
        if not isinstance(new_match, FootballMatch):
            raise TypeError("Expected a FootBallMatch instance")
        matches = match_file_manager.deserialize()
        matches.append(new_match)
        match_file_manager.serialize(matches)
    
    @staticmethod
    def del_match_from_file(match_id: str) -> None:
        if not isinstance(match_id, str):
            raise TypeError("match_id must be a string while deleting match from file")
        matches = match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == match_id]

        if suitable_matches:
            for match in suitable_matches:
                matches.remove(match)
            match_file_manager.serialize(matches)
        else:
            print(f"No match with id {match_id} found")

    @staticmethod
    def add_player_to_match(chosen_match_id: str, new_player_id: str) -> None:
        if not isinstance(chosen_match_id, str):
            raise TypeError("match_id must be a string while adding player to the match")
        if not isinstance(new_player_id, str):
            raise TypeError("new_player_id must be a string while adding to the match")
        
        players = player_file_manager.deserialize()
        if new_player_id not in [player.id for player in players]:
            raise ValueError("Player must be added to the players list before being added to a match")
        else:
            suitable_players = [player for player in players if player.id == new_player_id]
            new_player = suitable_players[0]
        matches = match_file_manager.deserialize()
        suitable_matches:list[FootballMatch] = [match for match in matches if match.id == chosen_match_id]
        new_match: FootballMatch
        print(suitable_matches)
        if suitable_matches:
            for new_match in suitable_matches:
                new_match.add_player(new_player)
            match_file_manager.serialize([new_match]) # type: ignore
        else:
            print(f"No match with id {chosen_match_id} found")
    
    @staticmethod
    def del_player_from_match(chosen_match_id: str, player_id: str) -> None:
        if not isinstance(chosen_match_id, str):
            raise TypeError("match_id must be a string while deleting player from the match")
        if not isinstance(player_id, str):
            raise TypeError("player_id must be a string while deleting player from the match")

        matches = match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == chosen_match_id]
    
        if suitable_matches:
            for match in suitable_matches:
                try:
                    match.remove_player(player_id)
                except ValueError as e:
                    print(f"No such player with id {player_id} found in match {chosen_match_id}: {e}")
        else:
            print(f"No match with id {chosen_match_id} found")
    
    @staticmethod
    def change_match_attribute(match_id: str, attribute: str, new_value) -> None:
        if not isinstance(match_id, str):
            raise TypeError("match_id must be a string")
        
        matches = match_file_manager.deserialize()
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
    
    @staticmethod
    def see_match_info(match_id: str) -> None:
        if not isinstance(match_id, str):
            raise TypeError("match_id must be a string while getting match info")
        matches = match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == match_id]
        
        if suitable_matches:
            for match in suitable_matches:
                print(match)
        else:
            print(f"No match with id {match_id} found")
    
    @staticmethod
    def sort_matches_by_date() -> None:
        matches = match_file_manager.deserialize()
        sorted_matches = sorted(matches, key=lambda match: match.match_date)
        match_file_manager.serialize(sorted_matches)
    
    @staticmethod
    def sort_matches_by_match_status() -> None:
        matches = match_file_manager.deserialize()
        sorted_matches = sorted(matches, key=lambda match: match.match_status)
        match_file_manager.serialize(sorted_matches)
    
    @staticmethod
    def print_all_matches() -> None:
        matches = match_file_manager.deserialize()
        for match in matches:
            print(match)

class StadiumService:
    @staticmethod
    def add_stadium_to_file(new_stadium: FootballStadium) -> None:
        if not isinstance(new_stadium, FootballStadium):
            raise TypeError("Expected a FootballStadium instance")
        stadiums = stadium_file_manager.deserialize()
        stadiums.append(new_stadium)
        stadium_file_manager.serialize(stadiums)

    @staticmethod
    def del_stadium_from_file(stadium_id: str) -> None:
        if not isinstance(stadium_id, str):
            raise TypeError("stadium_id must be a string while deleting stadium from file")
        stadiums = stadium_file_manager.deserialize()
        suitable_stadiums = [stadium for stadium in stadiums if stadium.id == stadium_id]
        
        if suitable_stadiums:
            for stadium in suitable_stadiums:
                stadiums.remove(stadium)
            stadium_file_manager.serialize(stadiums)
        else:
            print(f"No stadium with id {stadium_id} found")

    @staticmethod
    def change_stadium_attribute(stadium_id: str, attribute: str, new_value) -> None:
        if not isinstance(stadium_id, str):
            raise TypeError("stadium_id must be a string")

        stadiums = stadium_file_manager.deserialize()
        suitable_stadiums = [stadium for stadium in stadiums if stadium.id == stadium_id]

        if suitable_stadiums:
            for stadium in suitable_stadiums:
                if not hasattr(stadium, attribute):
                    raise AttributeError(f"Stadium does not have an attribute '{attribute}'")
                try:
                    setattr(stadium, attribute, new_value)
                except TypeError as e:
                    print(f"TypeError occurred while change_stadium_attribute '{attribute}': {e}")
                except ValueError as e:
                    print(f"ValueError occurred while change_stadium_attribute '{attribute}': {e}")
            stadium_file_manager.serialize(stadiums)
        else:
            print(f"No stadium with id {stadium_id} found")

    @staticmethod
    def add_match_to_stadium(stadium_id: str, match_id: str) -> None:
        if not isinstance(stadium_id, str):
            raise TypeError("stadium_id must be a string while adding match to stadium")
        if not isinstance(match_id, str):
            raise TypeError("Expected a FootballMatch instance while adding match to stadium")
        
        stadiums = stadium_file_manager.deserialize()
        suitable_stadiums = [stadium for stadium in stadiums if stadium.id == stadium_id]
        
        matches = match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.id == match_id]
        if not suitable_matches:
            raise ValueError("Match must be added to the matches list before being added to a stadium")
        else:
            new_match = suitable_matches[0]
        
        if suitable_stadiums:
            for stadium in suitable_stadiums:
                stadium.football_match = new_match
            stadium_file_manager.serialize(stadiums)
        else:
            print(f"No stadium with id {stadium_id} found")

    @staticmethod
    def stadium_info(stadium_id: str) -> None:
        if not isinstance(stadium_id, str):
            raise TypeError("stadium_id must be a string while getting stadium info")
        stadiums = stadium_file_manager.deserialize()
        suitable_stadiums = [stadium for stadium in stadiums if stadium.id == stadium_id]
        
        if suitable_stadiums:
            for stadium in suitable_stadiums:
                print(stadium)
        else:
            print(f"No stadium with id {stadium_id} found")
    
    @staticmethod
    def print_all_stadiums() -> None:
        stadiums = stadium_file_manager.deserialize()
        for stadium in stadiums:
            print(stadium)

class SearchEngine:
    @staticmethod
    def find_player_by_name_or_surname(name_or_surname: str) -> None:
        if not isinstance(name_or_surname, str):
            raise TypeError("name_or_surname must be a string while searching for player")
        players = player_file_manager.deserialize()
        suitable_players = [player for player in players if player.name == name_or_surname or player.surname == name_or_surname]
        
        if suitable_players:
            for player in suitable_players:
                print(player)
        else:
            print(f"No player with name or surname '{name_or_surname}' found")
    
    @staticmethod
    def find_match_by_date_and_opponent(match_date: str, opponent_team: str) -> None:
        if not isinstance(match_date, str):
            raise TypeError("match_date must be a string while searching for match")
        if not isinstance(opponent_team, str):
            raise TypeError("opponent_team must be a string while searching for match")
        matches = match_file_manager.deserialize()
        suitable_matches = [match for match in matches if match.match_date == match_date and match.away_team == opponent_team]
        
        if suitable_matches:
            for match in suitable_matches:
                print(match)
        else:
            print(f"No match on date '{match_date}' with opponent team '{opponent_team}' found")

    @staticmethod
    def find_stadium_by_name(stadium_name: str) -> None:
        if not isinstance(stadium_name, str):
            raise TypeError("stadium_name must be a string while searching for stadium")
        stadiums = stadium_file_manager.deserialize()
        suitable_stadiums = [stadium for stadium in stadiums if stadium.stadium_name == stadium_name]
        
        if suitable_stadiums:
            for stadium in suitable_stadiums:
                print(stadium)
        else:
            print(f"No stadium with name '{stadium_name}' found")
