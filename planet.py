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
        return f"Name: {self.name}, Climate: {self.climate}, Population: {self.population}"
    def to_dict(self):
        return {"name":self.name, "Climate":f"{self.climate}", "Population":self.population}
    def from_dict(cls, dict_data):
        return cls(name=dict_data["name"], 
                rotation_period=None,
                orbital_period=None,
                diameter=None,
                climate=dict_data["Climate"],
                gravity=None,
                terrain=None,
                surface_water=None,
                population=dict_data["Population"],
                url=None
                )
