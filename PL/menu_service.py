import os
from time import sleep
from DAL.Entities.football_match import FootballMatch
from DAL.Entities.football_player import FootballPlayer
from DAL.Entities.football_stadium import FootballStadium

from BLL.entity_services import PlayerService, StadiumService, MatchService

player_service = PlayerService()
stadium_service = StadiumService()
match_service = MatchService()

class MenuService:
    main_menu_choice = {1: "Manage players",
                        2: "Manage stadiums",
                        3: "Manage matches",
                        4: "Search entities",
                        5: "Exit"}

    player_menu_choice = {1: "Add player",
                          2: "Delete player by id",
                          3: "Update player attributes(name, surname, birth_date, status, health, salary)",
                          4: "View player by id",
                          5: "View all players",
                          6: "Back to Main Menu"}
    
    match_menu_choice = {1: "Add match",
                         2: "Delete match by id",
                         3: "View match by id",
                         4: "View all matches",
                         5: "Add player by id to match",
                         6: "Remove player by id from match",
                         7: "Update match attributes(match_place, home_team, away_team, match_date)",
                         8: "Sort matches by date",
                         9: "Sort matches by status",
                         10: "Back to Main Menu"}

    stadium_menu_choice = {1: "Add stadium",
                           2: "Delete stadium by id",
                           3: "Update stadium attributes(seats_amount, price_for_place)",
                           4: "View stadium info by id",
                           5: "View all stadiums info",
                           6: "Back to Main Menu"}
    @classmethod
    def _initialize_commands(cls) -> None:
        cls.main_menu_commands = [cls._display_player_menu,
                                   cls._display_stadium_menu,
                                   cls._display_match_menu,
                                   print("Search entities - Not implemented yet"),
                                   cls.exit_program]
        
        cls.player_menu_commands = [player_service.add_player_to_file,
                                    player_service.del_player_from_file,
                                    player_service.change_player_attribute,
                                    player_service.player_info,
                                    player_service.list_all_players,
                                    cls._display_main_menu]

        cls.match_menu_commands = [match_service.add_match_to_file,
                                   match_service.del_match_from_file,
                                   match_service.see_match_info,
                                   match_service.print_all_matches,
                                   match_service.add_player_to_match,
                                   match_service.del_player_from_match,
                                   match_service.change_match_attribute,
                                   match_service.sort_matches_by_date,
                                   match_service.sort_matches_by_match_status,
                                   cls._display_main_menu]
        
        cls.stadium_menu_commands = [stadium_service.add_stadium_to_file,
                                     stadium_service.del_stadium_from_file,
                                     stadium_service.change_stadium_attribute,
                                     stadium_service.stadium_info,
                                     stadium_service.print_all_stadiums,
                                     cls._display_main_menu]
    
    @classmethod
    def _display_main_menu(cls) -> int | None:
        print("=== Football Management System ===")
        for key, value in cls.main_menu_choice.items():
            print(f"{key}. {value}")
        choice = cls._right_input(cls.main_menu_choice)
        return choice

    @classmethod
    def _display_player_menu(cls) -> int | None:
        print("=== Player Management ===")
        for key, value in cls.player_menu_choice.items():
            print(f"{key}. {value}")
        choice = cls._right_input(cls.player_menu_choice)
        return choice

    @classmethod
    def _display_stadium_menu(cls) -> int | None:
        print("=== Stadium Management ===")
        for key, value in cls.stadium_menu_choice.items():
            print(f"{key}. {value}")
        choice = cls._right_input(cls.stadium_menu_choice)
        return choice

    @classmethod
    def _display_match_menu(cls) -> int | None:
        print("=== Match Management ===")
        for key, value in cls.match_menu_choice.items():
            print(f"{key}. {value}")
        choice = cls._right_input(cls.match_menu_choice)
        return choice

    @classmethod
    def _right_input(cls, menu_type: dict) -> int | None:
        choose_action = input("Enter your choice: ")
        print("Choice =", choose_action, choose_action in menu_type)
        print("Menu type", menu_type)
        if not choose_action.isdigit():
            print("Action number must be a digit")
            return None
        int_choice = int(choose_action)
        if not int_choice in menu_type:
            print("Action must be from available list")
            return None
        return int_choice

    @classmethod
    def run_main_menu(cls) -> None:
        cls._initialize_commands()
        while True:
            os.system('clear')
            main_menu_choice = cls._display_main_menu()
            sleep(0.3)
            os.system('clear')
            if main_menu_choice:
                some_menu_choice = cls.main_menu_commands[main_menu_choice - 1]()
                sleep(0.3)
                os.system('clear')
                if some_menu_choice:
                    if main_menu_choice == 1:
                        cls.player_menu_commands[some_menu_choice - 1]()
                    elif main_menu_choice == 2:
                        cls.stadium_menu_commands[some_menu_choice - 1]()
                    elif main_menu_choice == 3:
                        cls.match_menu_commands[some_menu_choice - 1]()
                    sleep(0.3)
                    os.system('clear')
            else:
                print("Invalid choice. Please try again.")
                sleep(0.3)

    @staticmethod
    def exit_program() -> None:
        print("Exiting the program. Goodbye!")
        exit(0)