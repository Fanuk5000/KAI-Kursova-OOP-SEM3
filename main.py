from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_mathes import FootBallMatch
from DAL.file_manipulation import PlayerFileManager

def main():
    # temporary test code
    file_manager = PlayerFileManager("football_players.json")

    players = [
        FootballPlayer("Lionel", "Messi", "24-06-1987", "Active", 95, 500000.0),
        FootballPlayer("Cristiano", "Ronaldo", "05-02-1985", "Active", 90, 450000.0),
    ]
    match = FootBallMatch("TeamA", "TeamB", "2024-10-15", "2-1")
    match.add_player(players[0])
    file_manager.serialize(players)

    loaded_players = file_manager.deserialize()
    if loaded_players:
        for player in loaded_players:
            print(player)


if __name__ == "__main__":
    main()