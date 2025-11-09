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
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        else:
            print("MenuService instance already exists. Returning the existing instance.")
        return cls.__instance
    
    def __del__(self):
        MenuService.__instance = None

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
        
        cls.player_menu_commands = [cls._add_player_to_file,
                                    cls._remove_player_from_file,
                                    cls._change_player_attribute,
                                    cls._view_player_info,
                                    player_service.list_all_players,
                                    cls._display_main_menu]

        cls.match_menu_commands = [cls._add_match_to_file,
                                   cls._remove_match_from_file,
                                   cls._view_match_info,
                                   match_service.print_all_matches,
                                   cls._add_player_to_match,
                                   cls._remove_player_from_match,
                                   cls._change_match_attribute,
                                   match_service.sort_matches_by_date,
                                   match_service.sort_matches_by_match_status,
                                   cls._display_main_menu]
        
        cls.stadium_menu_commands = [cls._add_stadium_to_file,
                                     cls._remove_stadium_from_file,
                                     cls._change_stadium_attribute,
                                     cls._view_stadium_info,
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
        if not choose_action.isdigit():
            print("Action number must be a digit")
            return None
        int_choice = int(choose_action)
        if not int_choice in menu_type:
            print("Action must be from available list")
            return None
        return int_choice
    
    # --------------- File iteration methods ---------------
    # Player methods ---------------------------------------

    @classmethod
    def _add_player_to_file(cls) -> None:
        new_instance = input("Enter name, surname, birth date, status, health, salary (space separated): ").split()
        if len(new_instance) != 6:
            print("Invalid input. Please provide exactly 6 values.")
            return
        new_instance = [float(value) if value.isdigit() else value for value in new_instance ]
        try:
            football_player = FootballPlayer(*new_instance) # type: ignore
        except (TypeError, ValueError) as e:
            print(f"Error creating FootballPlayer: {e}")
            return
        player_service.add_player_to_file(football_player)
    
    @classmethod
    def _remove_player_from_file(cls) -> None:
        chosen_player_id = input("Enter player id: ")
        try:
            player_service.del_player_from_file(chosen_player_id)
        except TypeError as e:
            print(f"Wrong type provided: {e}")
    
    @classmethod
    def _change_player_attribute(cls) -> None:
        player_id = input("Enter player id: ")
        player_atribute = input("Enter player attribute to change (name, surname, birth_date, status, health, salary): ")
        new_value = input("Enter new value: ")

        if new_value.replace('.', '', 1).isdigit() and '.' not in new_value:
            new_value = int(new_value)
        else:
            new_value = float(new_value) if new_value.replace('.', '', 1).isdigit() else new_value

        try:
            player_service.change_player_attribute(player_id, player_atribute, new_value)
        except (TypeError, ValueError) as e:
            print(f"Error changing player attribute: {e}")
    
    @classmethod
    def _view_player_info(cls) -> None:
        player_id = input("Enter player id: ")
        try:
            player_service.player_info(player_id)
        except (TypeError, ValueError) as e:
            print(f"Error viewing player info: {e}")

    # Match methods ---------------------------------------
    @classmethod
    def _add_match_to_file(cls) -> None:
        new_instance = input("Enter match_place, home_team, away_team, match_date, match_status, score, players, viewers (space separated): ").split()
        if len(new_instance) < 5:
            print("Invalid input. Please provide exactly 8 values.")
            return
        new_instance = [float(value) if value.isdigit() else value for value in new_instance ]
        try:
            football_match = FootballMatch(*new_instance) # type: ignore
        except (TypeError, ValueError) as e:
            print(f"Error creating FootballMatch: {e}")
            return
        match_service.add_match_to_file(football_match)
    
    @classmethod
    def _remove_match_from_file(cls) -> None:
        chosen_match_id = input("Enter match id: ")
        try:
            match_service.del_match_from_file(chosen_match_id)
        except TypeError as e:
            print(f"Wrong type provided: {e}")
    
    @classmethod
    def _view_match_info(cls) -> None:
        match_id = input("Enter match id: ")
        try:
            match_service.see_match_info(match_id)
        except (TypeError, ValueError) as e:
            print(f"Error viewing match info: {e}")

    @classmethod
    def _add_player_to_match(cls) -> None:
        match_id = input("Enter match id: ")
        player_id = input("Enter player id: ")
        try:
            match_service.add_player_to_match(match_id, player_id)
        except (TypeError, ValueError) as e:
            print(f"Error adding player to match: {e}")

    @classmethod
    def _remove_player_from_match(cls) -> None:
        match_id = input("Enter match id: ")
        player_id = input("Enter player id: ")
        try:
            match_service.del_player_from_match(match_id, player_id)
        except (TypeError, ValueError) as e:
            print(f"Error removing player from match: {e}")

    @classmethod
    def _change_match_attribute(cls) -> None:
        match_id = input("Enter match id: ")
        match_attribute = input("Enter match attribute to change (match_place, home_team, away_team, match_date, match_status, score, players, viewers): ")
        new_value = input("Enter new value: ")

        if new_value.replace('.', '', 1).isdigit() and '.' not in new_value:
            new_value = int(new_value)
        else:
            new_value = float(new_value) if new_value.replace('.', '', 1).isdigit() else new_value
        
        try:
            match_service.change_match_attribute(match_id, match_attribute, new_value)
        except (TypeError, ValueError) as e:
            print(f"Error changing match attribute: {e}")
    # Stadium methods ---------------------------------------
    @classmethod
    def _add_stadium_to_file(cls) -> None:
        new_instance = input("Enter stadium_name, seats_amount, price_for_place (space separated): ").split()
        if len(new_instance) != 3:
            print("Invalid input. Please provide exactly 3 values.")
            return
        new_instance = [
            float(value) if value.replace('.', '', 1).isdigit() and '.' in value
            else int(value) if value.isdigit()
            else value
            for value in new_instance
        ]
        try:
            football_stadium = FootballStadium(*new_instance) # type: ignore
        except (TypeError, ValueError) as e:
            print(f"Error creating FootballStadium: {e}")
            return
        stadium_service.add_stadium_to_file(football_stadium)
    
    @classmethod
    def _remove_stadium_from_file(cls) -> None:
        chosen_stadium_id = input("Enter stadium id: ")
        try:
            stadium_service.del_stadium_from_file(chosen_stadium_id)
        except TypeError as e:
            print(f"Wrong type provided: {e}")
    
    @classmethod
    def _change_stadium_attribute(cls) -> None:
        stadium_id = input("Enter stadium id: ")
        stadium_attribute = input("Enter stadium attribute to change (seats_amount, price_for_place): ")
        new_value = input("Enter new value: ")

        if new_value.replace('.', '', 1).isdigit() and '.' not in new_value:
            new_value = int(new_value)
        else:
            new_value = float(new_value) if new_value.replace('.', '', 1).isdigit() else new_value
        
        try:
            stadium_service.change_stadium_attribute(stadium_id, stadium_attribute, new_value)
        except (TypeError, ValueError) as e:
            print(f"Error changing stadium attribute: {e}")
    
    @classmethod
    def _view_stadium_info(cls) -> None:
        stadium_id = input("Enter stadium id: ")
        try:
            stadium_service.stadium_info(stadium_id)
        except (TypeError, ValueError) as e:
            print(f"Error viewing stadium info: {e}")
    # -------------------------------------------------------
    @classmethod
    def run_main_menu(cls) -> None:
        cls._initialize_commands()
        TIME_SLEEP = 2
        while True:
            os.system('clear')
            main_menu_choice = cls._display_main_menu()
            sleep(TIME_SLEEP)
            os.system('clear')
            if main_menu_choice:
                some_menu_choice = cls.main_menu_commands[main_menu_choice - 1]()
                sleep(TIME_SLEEP)
                os.system('clear')
                if some_menu_choice:
                    if main_menu_choice == 1:
                        cls.player_menu_commands[some_menu_choice - 1]()
                    elif main_menu_choice == 2:
                        cls.stadium_menu_commands[some_menu_choice - 1]()
                    elif main_menu_choice == 3:
                        cls.match_menu_commands[some_menu_choice - 1]()
                    sleep(TIME_SLEEP)
                    os.system('clear')
            else:
                print("Invalid choice. Please try again.")
                sleep(TIME_SLEEP)

    @staticmethod
    def exit_program() -> None:
        print("Exiting the program. Goodbye!")
        exit(0)