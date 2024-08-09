class Vehicle:
    vehicle_list = []

    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class, pilots, films, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.vehicle_class = vehicle_class
        self.pilots = pilots  # Lista de URLs
        self.films = films  # Lista de URLs
        self.url = url
        Vehicle.vehicle_list.append(self)

    def __str__(self):
        return f"Name: {self.name}, Model: {self.model}, Manufacturer: {self.manufacturer}"
