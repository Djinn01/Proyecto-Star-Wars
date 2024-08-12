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
        return f"Name: {self.name}, Model: {self.model}, Manufacturer: {self.manufacturer}"

    def to_dict(self):
        return {"name":self.name, 
                "model":self.model,
                "manufacturer": self.manufacturer
            }   
    def from_dict(cls, dict_data):
        return cls(name=dict_data["name"], 
                    model=dict_data["model"], 
                    manufacturer=dict_data["manufacturer"],
                    cost_in_credits=None,
                    length=None,
                    max_atmosphering_speed=None,
                    crew=None,
                    passengers=None,
                    cargo_capacity=None,
                    consumables=None,
                    hyperdrive_rating=None,
                    MGLT=None,
                    starship_class=None,
                    pilots=None,
                    url=None
                    )
