class Planet:
    planet_list = []
#definir la clase
    def __init__(self, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population, url):
        self.name = name
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.url = url
        Planet.planet_list.append(self)
#funciones para cambiar de objetos a diccionarios y vice versa para poder subir y cargar los datos del txt
    def __str__(self):
        return f"Name: {self.name}, rotation period: {self.rotation_period}, orbital period: {self.orbital_period}, diameter: {self.diameter}, Climate: {self.climate}, gravity: {self.gravity}, terrain: {self.terrain}, surface water: {self.surface_water}, Population: {self.population}, url: {self.url}"
    def to_dict(self):
        return {"Name": {self.name}, "rotation period": self.rotation_period, "orbital period": self.orbital_period, "diameter": self.diameter, "Climate": self.climate, "gravity": self.gravity, "terrain": self.terrain, "surface water": self.surface_water, "Population": self.population, "url": self.url}
    def from_dict(cls, dict_data):
        return cls(name=dict_data["name"], 
                rotation_period=dict_data["rotation period"],
                orbital_period=dict_data["orbital period"],
                diameter=dict_data["diameter"],
                climate=dict_data["Climate"],
                gravity=dict_data["gravity"],
                terrain=dict_data["terrain"],
                surface_water=dict_data["surface water"],
                population=dict_data["Population"],
                url=dict_data["url"]
                )
