from PL.menu_service import MenuService

def main() -> None:
    try:
        MenuService.run_main_menu()
    except KeyboardInterrupt:
        to_exit = input("\nDo you really want to exit? (y/n): ")
        if to_exit.lower() in {'y', 'yes', "ye"}:
            print("Exiting the program. Goodbye!")
            exit(0)
        else:
            main()

if __name__ == "__main__":
    main()