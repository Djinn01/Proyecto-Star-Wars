import menu
from planet import Planet
from people import People
from starship import Starship
from missions import Missions
import json

#funcion de guardado al txt
def save_missions():
    if len(Missions.mission_list) == 0:
        print("No missions to save.")
        return
    with open("missions.txt", "w") as f:
        for obj in Missions.mission_list:
            to_d = Missions.to_dict(obj)
            f.write(str(to_d) + "\n")
#funcion de cargar los datos del txt
def load_missions():
    Missions.mission_list = []
    with open("missions.txt", "r") as f:
        for line in f:
            mission_dict = eval(line.strip())
            print(mission_dict)
            mis = Missions.from_dict(Missions, mission_dict)
            Missions.mission_list.append(mis)
#funcion de edicion de planetas para las misiones
def edit_mission_planet():
    while True:
        for planet in Planet.planet_list:
            print(f"{planet.name}")
        mission_planet = input("Enter the mission destination: ")
        for planet in Planet.planet_list:
            if planet.name == mission_planet:
                return planet
        else:
            print("Invalid planet name. Please try again.")
            continue
    return mission_planet
#funcion de edicion del equipo para las misiones
def edit_crew():
    crew_list = []
    while True:
        for person in People.people_list:
            print(f"{person.name}")
        if len(crew_list) == 7:
            print("Maximum number of crew members reached. Cannot add more.")
            return crew_list
        else:
            while True:
                crew_person = input("Enter the name of a crew member: ")
                for person in People.people_list:
                    if person.name == crew_person:
                        crew_list.append(person)
                        while True:
                            choice = input(f"Do you want to add another crew member \n1. yes\n2. no")
                            if choice == "1":
                                break
                            elif choice == "2":
                                return crew_list
                            else:
                                print("Invalid choice. Please try again.")
                                continue
                print("Invalid crew member name. Please try again.")
                continue
#funcion de edicion de armas para usar en las misiones
def edit_weapons():
    weapons = ["light saber", "slugthrower", "blaster pistol", "blaster rifle", "disruptor", "sniper rifle", "rocket launcher"]
    weapon_list = []
    while True:
        for weapon in weapons:
            print(f"\n {weapon}")
        if len(weapon_list) == 7:
            print("Maximum number of weapons reached. Cannot add more.")
            return weapon_list
        else:
            weapon_name = input("Enter the name of a weapon: ")
            for weapon in weapons:
                if weapon == weapon_name:
                    weapon_list.append(weapon)
                    while True:
                        choice = input(f"Do you want to add another weapon \n1. yes\n2. no")
                        if choice == "1":
                            break
                        elif choice == "2":
                            return weapon_list
                        else:
                            print("Invalid choice. Please try again.")
                            continue
            print("invalid weapon. Please try again.")
            continue
#funcion de edicion de naves para las misiones
def edit_mission_ship():
    while True:
        for ship in Starship.starship_list:
            print(f"{ship.name}")
        mission_ship = input("Enter the mission ship: ")
        for ship in Starship.starship_list:
            if ship.name == mission_ship:
                return ship
        else:
            print("Invalid ship name. Please try again.")
            continue
#funcion de edicion del nombre de la mision
def edit_mission_name():
    mission_name = input("Enter the mission name: ")
    if len(Missions.mission_list) == 0:
        return mission_name
    else:
        for mission in Missions.mission_list:
            if mission.name == mission_name:
                print("Mission name already exists. Please choose a different name.")
                edit_mission_name()
    return mission_name
#funcion para crear misiones
def create_mission():
    if len(Missions.mission_list) >= 5:
        print("you can not create more missions")
    else:
        mission_planet = edit_mission_planet()
        crew_list = edit_crew()
        weapon_list = edit_weapons()
        mission_ship = edit_mission_ship()
        mission_name = edit_mission_name()
        Missions.mission_list.append(Missions(mission_name, mission_planet, mission_ship, weapon_list, crew_list))
        print("mission succesfully created")
#funcion para visualisar las misiones activas
def view_active_mission():
    if len(Missions.mission_list) == 0:
        print("No active missions.")
        return
    for obj in Missions.mission_list:
        print(f"\nMission Name: {obj.name}")
        print(f"Planet: {obj.planet}")
        print(f"Ship: {obj.ship}")
        print(f"Crew:")
        for x in obj.crew:
            print(f"{x}")
        print(f"Weapons:")
        for x in obj.weapons:
            print(f"{x}")
#funcion para modificar funciones
def modify_mission():
    if len(Missions.mission_list) == 0:
        print("No missions to modify.")
        return
    else:
        for mission in Missions.mission_list:
            print(f"\nMission Name: {mission.name}")
        while True:
            mission_name = input("Enter the name of the mission to modify: ")
            for mission in Missions.mission_list:
                if mission.name == mission_name:
                    print("\nModifying mission...")
                    mission.planet = edit_mission_planet()
                    mission.crew = edit_crew()
                    mission.weapons = edit_weapons()
                    mission.ship = edit_mission_ship()
                    return
            else:
                print("Invalid mission name. Please try again.")
#funcion para administrar todo sobre las misiones
def mission_admin():
    while True:
        print("\nMission Administration Menu:")
        print("1. Create a mission")
        print("2. Modify a mission")
        print("3. See active missions")
        print("4. Save current missions")
        print("5. Load missions (Will overwrite existing missions)")
        print("6. Exit")
        choice = input("")
        if choice == "1":
            print("\nCreating a new mission...")
            create_mission()
        if choice == "2":
            modify_mission()
        if choice == "3":
            view_active_mission()
        if choice == "4":
            save_missions()
        if choice == "5":
            load_missions()
        if choice == "6":
            menu.main_menu()
