from loader import load_films, load_people, load_planets, load_starships, load_vehicles, load_species
from film import Film
from people import People
from vehicle import Vehicle
from starship import Starship
from species import Species
from planet import Planet

import menu

def main():
    print("Loading films...")
    load_films()
    print(f"Loaded {len(Film.film_list)} films.")

    print("Loading people...")
    load_people()
    print(f"Loaded {len(People.people_list)} people.")

    print("Loading planets...")
    load_planets()
    print(f"Loaded {len(Planet.planet_list)} planets.")

    print("Loading starships...")
    load_starships()
    print(f"Loaded {len(Starship.starship_list)} starships.")

    print("Loading vehicles...")
    load_vehicles()
    print(f"Loaded {len(Vehicle.vehicle_list)} vehicles.")

    print("Loading species...")
    load_species()
    print(f"Loaded {len(Species.species_list)} species.")

    menu.main_menu()

if __name__ == "__main__":
    main()
