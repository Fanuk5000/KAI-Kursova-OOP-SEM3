from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_match import FootballMatch
from DAL.file_manipulations import PlayerFileManager
from DAL.file_manipulations import MatchFileManager

def main():
    # temporary test code
    player_file_manager = PlayerFileManager("football_players.json")
    match_file_manager = MatchFileManager("football_matches.json")

    players = [
        FootballPlayer("Lionel", "Messi", "24-06-1987", "Active", 95, 500000.0),
        FootballPlayer("Cristiano", "Ronaldo", "05-02-1985", "Active", 90, 450000.0),
    ]
    match = FootballMatch("Ukraine", "TeamA", "TeamB", "24-06-1987", "2:1")
    match.add_player(players[0])
    player_file_manager.serialize(players)

    loaded_players = player_file_manager.deserialize()
    if loaded_players:
        for player in loaded_players:
            print(player)

    match_file_manager.serialize([match])

    loaded_matches = match_file_manager.deserialize()
    if loaded_matches:
        for match in loaded_matches:
            print(match)

if __name__ == "__main__":
    main()