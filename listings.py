import menu
from film import Film
from species import Species
from planet import Planet
from people import People
from starship import Starship
from vehicle import Vehicle
#ver attributos de las peliculas
def view_films():
    for film in Film.film_list:
        print(f"\nTitle: {film.title}")
        print(f"Episode Number: {film.episode_id}")
        print(f"Release Date: {film.release_date}")
        print(f"Opening Crawl: {film.opening_crawl}")
        print(f"Director: {film.director}")
    input("\nPress Enter to return to the listings menu...")
    menu.view_listings_menu()
#ver atributos de los tipos de especies
def view_species():
    species_list_sorted = sorted(Species.species_list, key=lambda x: x.url)

    for species in species_list_sorted:
        print(f"\nName: {species.name}")
        print(f"Average Height: {species.average_height}")
        print(f"Classification: {species.classification}")

        homeworld_name = "Unknown"
        for planet in Planet.planet_list:
            if planet.url == species.homeworld:
                homeworld_name = planet.name
                break 
        print(f"Homeworld: {homeworld_name}")

        print(f"Language: {species.language}")

        people_names = [person.name for person in People.people_list if person.url in species.people]
        print(f"Characters: {', '.join(people_names) if people_names else 'None'}")

        film_titles = [f"{film.title}, episode {film.episode_id}" for film in Film.film_list if species.url in film.species]
        print(f"Episodes: {', '.join(film_titles) if film_titles else 'None'}")

    input("\nPress Enter to return to the listings menu...")
    menu.view_listings_menu()
#ver atributos de los planetas
def view_planets():
    for planet in Planet.planet_list:
        print(f"\nName: {planet.name}")
        print(f"Orbital Period: {planet.orbital_period}")
        print(f"Rotation Period: {planet.rotation_period}")
        print(f"Population: {planet.population}")
        print(f"Climate: {planet.climate}")

        people_names = [person.name for person in People.people_list if person.homeworld == planet.url]
        print(f"Characters: {', '.join(people_names) if people_names else 'None'}")

        film_titles = [f"{film.title}, episode {film.episode_id}" for film in Film.film_list if planet.url in film.planets]
        print(f"Episodes: {', '.join(film_titles) if film_titles else 'None'}")

    input("\nPress Enter to return to the listings menu...")
    menu.view_listings_menu()
#buscar personajes de la franquicia con una busqueda a caracteres
def search_character():
    search_query = input("Enter the character name or part of the name to search: ").lower()
    matching_characters = [person for person in People.people_list if search_query in person.name.lower()]

    if not matching_characters:
        print("No matching characters found.")
    else:
        for person in matching_characters:
            print(f"\nName: {person.name}")

            homeworld_name = "Unknown"
            for planet in Planet.planet_list:
                if planet.url == person.homeworld:
                    homeworld_name = planet.name
                    break
            print(f"Homeworld: {homeworld_name}")

            film_titles = [f"{film.title}, episode {film.episode_id}" for film in Film.film_list if person.url in film.characters]
            print(f"Episodes: {', '.join(film_titles) if film_titles else 'None'}")

            print(f"Gender: {person.gender}")

            species_name = "Unknown"
            for species in Species.species_list:
                if person.url in species.people:
                    species_name = species.name
                    break
            print(f"Species: {species_name}")

            starship_names = [starship.name for starship in Starship.starship_list if person.url in starship.pilots]
            print(f"Starships: {', '.join(starship_names) if starship_names else 'None'}")

            vehicle_names = [vehicle.name for vehicle in Vehicle.vehicle_list if person.url in vehicle.pilots]
            print(f"Vehicles: {', '.join(vehicle_names) if vehicle_names else 'None'}")

    input("\nPress Enter to return to the listings menu...")
    menu.view_listings_menu()
