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
        return f"name: {self.name}, height: {self.height}, mass: {self.mass}, hair color:{self.hair_color}, skin color:{self.skin_color}, eye color: {self.eye_color}, birth year: {self.birth_year}, gender: {self.gender}, homeworld: {self.homeworld}, url: {self.url}"
    def to_dict(self):
        crew = []
        for person in self:
            crew.append({"name":person.name,
                    "height":person.height,
                    "mass":person.mass,
                    "hair color":person.hair_color,
                    "skin color":person.skin_color,
                    "eye color":person.eye_color,
                    "birth year":person.birth_year,
                    "gender":person.gender, 
                    "homeworld":person.homeworld,
                    "url":person.url
                    })
        return crew
    def from_dict(cls, dict_data):
        crew = []
        for person in dict_data:
            crew.append(cls(name=person["name"], 
                        height=person["heigh"],
                        mass=person["mass"],
                        hair_color=person["hair color"],
                        skin_color=person["skin color"],
                        eye_color=person["eye color"],
                        birth_year=person["birth year"],
                        gender=person["gender"], 
                        homeworld=person["homeworld"],
                        url=person["url"]
                        ))
        return crew
