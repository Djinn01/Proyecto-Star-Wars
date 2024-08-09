class Planet:
    planet_list = []

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

    def __str__(self):
        return f"Name: {self.name}, Climate: {self.climate}, Population: {self.population}"
