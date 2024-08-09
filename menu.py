import sys
from listings import view_films, view_species, view_planets, search_character

def main_menu():
    print("Welcome to Star Wars Explorer!")
    print("1. View Listings")
    print("2. View Statistics")
    print("3. View Missions")
    print("4. Exit")

    choice = input("Please choose an option: ")

    if choice == '1':
        view_listings_menu()
    elif choice == '2':
        view_statistics_menu()
    elif choice == '3':
        view_missions_menu()
    elif choice == '4':
        exit_program()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def view_listings_menu():
    print("\n--- View Listings ---")
    print("1. Films")
    print("2. Species")
    print("3. Planets")
    print("4. Search Character")
    print("5. Back to Main Menu")

    choice = input("Please choose a listing to view: ")

    if choice == '1':
        view_films()
    elif choice == '2':
        view_species()
    elif choice == '3':
        view_planets()
    elif choice == '4':
        search_character()
    elif choice == '5':
        main_menu()
    else:
        print("Invalid choice, please try again.")
        view_listings_menu()

def view_statistics_menu():
    print("\n--- View Statistics ---")
    print("Statistics menu is currently empty.")
    main_menu()

def view_missions_menu():
    print("\n--- View Missions ---")
    print("Missions menu is currently empty.")
    main_menu()

def exit_program():
    print("Exiting the program. May the Force be with you!")
    sys.exit()

if __name__ == "__main__":
    main_menu()
