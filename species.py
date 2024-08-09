class Species:
    species_list = []

    def __init__(self, name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, homeworld, language, people, url):
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.skin_colors = skin_colors
        self.hair_colors = hair_colors
        self.eye_colors = eye_colors
        self.average_lifespan = average_lifespan
        self.homeworld = homeworld  # URL
        self.language = language
        self.people = people  # Lista de URLs
        self.url = url
        Species.species_list.append(self)

    def __str__(self):
        return f"Name: {self.name}, Classification: {self.classification}, Language: {self.language}"
