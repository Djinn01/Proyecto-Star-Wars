from people import People
from planet import Planet
from starship import Starship
#definir la clase
class Missions:
    mission_list = []
    def __init__(self, name, planet, ship, weapons, crew):
        self.name = name
        self.planet = planet
        self.ship = ship
        self.weapons = weapons
        self.crew = crew
#funciones para cambiar de objetos a diccionarios y vice versa para poder subir y cargar los datos del txt
    def to_dict(self):
        planet = Planet.to_dict(self.planet)
        ship = Starship.to_dict(self.ship)
        crew = People.to_dict(self.crew)
        return {"name":self.name, 
                "planet":planet,
                "ship":ship, 
                "weapons":self.weapons, 
                "crew":crew
                }
    def from_dict(cls, dict_data):
            planet = Planet.from_dict(Planet, dict_data["planet"])
            crew = People.from_dict(People, dict_data["crew"])
            ship = Starship.from_dict(Starship, dict_data["ship"])
            return cls(name=dict_data["name"], 
                        planet=planet, 
                        ship=ship, 
                        weapons=dict_data["weapons"], 
                        crew=crew
                        )
