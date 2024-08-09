class People:
    people_list = []

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

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Birth Year: {self.birth_year}"
