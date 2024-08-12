class People:
    people_list = []
#definir la clase
    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, homeworld, url):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld  # URL
        self.url = url
        People.people_list.append(self)
#funciones para cambiar de objetos a diccionarios y vice versa para poder subir y cargar los datos del txt
    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Birth Year: {self.birth_year}"
    def to_dict(self):
        crew = []
        for person in self:
            crew.append({"name":person.name, 
                    "gender":person.gender, 
                    "birth year":person.birth_year 
                    })
        return crew
    def from_dict(cls, dict_data):
        crew = []
        for person in dict_data:
            crew.append(cls(name=person["name"], 
                        height=None,
                        mass=None,
                        hair_color=None,
                        skin_color=None,
                        eye_color=None,
                        gender=person["gender"], 
                        birth_year=person["birth year"],
                        homeworld=None,
                        url=None
                        ))
        return crew
