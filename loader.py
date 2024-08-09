import requests
from film import Film
from people import People
from planet import Planet
from starship import Starship
from vehicle import Vehicle
from species import Species

def load_films():
    url = "https://www.swapi.tech/api/films"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['result']:
            film_url = f"https://www.swapi.tech/api/films/{item['uid']}"
            film_data = requests.get(film_url).json()['result']['properties']
            Film(
                title=film_data['title'],
                episode_id=film_data['episode_id'],
                opening_crawl=film_data['opening_crawl'],
                director=film_data['director'],
                producer=film_data['producer'],
                release_date=film_data['release_date'],
                characters=film_data['characters'],
                planets=film_data['planets'],
                starships=film_data['starships'],
                vehicles=film_data['vehicles'],
                species=film_data['species']
            )
        url = data.get('next')

def load_people():
    url = "https://www.swapi.tech/api/people"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['results']:
            people_url = f"https://www.swapi.tech/api/people/{item['uid']}"
            people_data = requests.get(people_url).json()['result']['properties']
            People(
                name=people_data['name'],
                height=people_data['height'],
                mass=people_data['mass'],
                hair_color=people_data['hair_color'],
                skin_color=people_data['skin_color'],
                eye_color=people_data['eye_color'],
                birth_year=people_data['birth_year'],
                gender=people_data['gender'],
                homeworld=people_data['homeworld'],
                url=people_url
            )
        url = data.get('next')

def load_planets():
    url = "https://www.swapi.tech/api/planets"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['results']:
            planet_url = f"https://www.swapi.tech/api/planets/{item['uid']}"
            planet_data = requests.get(planet_url).json()['result']['properties']
            Planet(
                name=planet_data['name'],
                rotation_period=planet_data['rotation_period'],
                orbital_period=planet_data['orbital_period'],
                diameter=planet_data['diameter'],
                climate=planet_data['climate'],
                gravity=planet_data['gravity'],
                terrain=planet_data['terrain'],
                surface_water=planet_data['surface_water'],
                population=planet_data['population'],
                url=planet_url
            )
        url = data.get('next')

def load_starships():
    url = "https://www.swapi.tech/api/starships"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['results']:
            starship_url = f"https://www.swapi.tech/api/starships/{item['uid']}"
            starship_data = requests.get(starship_url).json()['result']['properties']
            Starship(
                name=starship_data['name'],
                model=starship_data['model'],
                manufacturer=starship_data['manufacturer'],
                cost_in_credits=starship_data['cost_in_credits'],
                length=starship_data['length'],
                max_atmosphering_speed=starship_data['max_atmosphering_speed'],
                crew=starship_data['crew'],
                passengers=starship_data['passengers'],
                cargo_capacity=starship_data['cargo_capacity'],
                consumables=starship_data['consumables'],
                hyperdrive_rating=starship_data['hyperdrive_rating'],
                MGLT=starship_data['MGLT'],
                starship_class=starship_data['starship_class'],
                pilots=starship_data['pilots'],
                url=starship_url
            )
        url = data.get('next')

def load_vehicles():
    url = "https://www.swapi.tech/api/vehicles"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['results']:
            vehicle_url = f"https://www.swapi.tech/api/vehicles/{item['uid']}"
            vehicle_data = requests.get(vehicle_url).json()['result']['properties']
            Vehicle(
                name=vehicle_data['name'],
                model=vehicle_data['model'],
                manufacturer=vehicle_data['manufacturer'],
                cost_in_credits=vehicle_data['cost_in_credits'],
                length=vehicle_data['length'],
                max_atmosphering_speed=vehicle_data['max_atmosphering_speed'],
                crew=vehicle_data['crew'],
                passengers=vehicle_data['passengers'],
                cargo_capacity=vehicle_data['cargo_capacity'],
                consumables=vehicle_data['consumables'],
                vehicle_class=vehicle_data['vehicle_class'],
                pilots=vehicle_data['pilots'],
                films=vehicle_data['films'],
                url=vehicle_url
            )
        url = data.get('next')

def load_species():
    url = "https://www.swapi.tech/api/species"
    while url:
        response = requests.get(url)
        data = response.json()
        for item in data['results']:
            species_url = f"https://www.swapi.tech/api/species/{item['uid']}"
            species_data = requests.get(species_url).json()['result']['properties']
            Species(
                name=species_data['name'],
                classification=species_data['classification'],
                designation=species_data['designation'],
                average_height=species_data['average_height'],
                skin_colors=species_data['skin_colors'],
                hair_colors=species_data['hair_colors'],
                eye_colors=species_data['eye_colors'],
                average_lifespan=species_data['average_lifespan'],
                homeworld=species_data['homeworld'],
                language=species_data['language'],
                people=species_data['people'],
                url=species_url
            )
        url = data.get('next')
