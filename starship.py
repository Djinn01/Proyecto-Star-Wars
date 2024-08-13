class Starship:
    starship_list = []
#definir la clase
    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, pilots, url):
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
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class = starship_class
        self.pilots = pilots  # Lista de URLs
        self.url = url
        Starship.starship_list.append(self)
#funciones para cambiar de objetos a diccionarios y vice versa para poder subir y cargar los datos del txt
    def __str__(self):
        return f"Name: {self.name}, Model: {self.model}, Manufacturer: {self.manufacturer}, Cost in credits: {self.cost_in_credits}, length: {self.length}, max atmosphering speed: {self.max_atmosphering_speed}, crew: {self.crew}, passengers: {self.passengers}, cargo capacity: {self.cargo_capacity}, consumables: {self.consumables}, hyperdrive rating:{self.hyperdrive_rating}, MGLT: {self.MGLT}, starship class: {self.starship_class}, pilots: {self.pilots}, url: {self.url}"

    def to_dict(self):
        return {"name":self.name, 
                "model":self.model,
                "manufacturer": self.manufacturer,
                "Cost in credits": self.cost_in_credits,
                "length": self.length,
                "max atmosphering speed": self.max_atmosphering_speed,
                "crew": self.crew,
                "passengers": self.passengers,
                "cargo capacity": self.cargo_capacity,
                "consumables": self.consumables,
                "hyperdrive rating": self.hyperdrive_rating,
                "MGLT": self.MGLT,
                "starship class": self.starship_class,
                "pilots": self.pilots,
                "url": self.url
            }   
    def from_dict(cls, dict_data):
        return cls(name=dict_data["name"], 
                    model=dict_data["model"], 
                    manufacturer=dict_data["manufacturer"],
                    cost_in_credits=dict_data["cost in credits"],
                    length=dict_data["length"],
                    max_atmosphering_speed=dict_data["max atmosphering speed"],
                    crew=dict_data["crew"],
                    passengers=dict_data["passengers"],
                    cargo_capacity=dict_data["cargo capacity"],
                    consumables=dict_data["consumables"],
                    hyperdrive_rating=dict_data["hyperdrive rating"],
                    MGLT=dict_data["MGLT"],
                    starship_class=dict_data["starship class"],
                    pilots=dict_data["pilots"],
                    url=dict_data["url"],
                    )
