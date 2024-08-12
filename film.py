class Film:
    film_list = []
#definir la clase
    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships, vehicles, species):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.characters = characters  # Lista de URLs
        self.planets = planets  # Lista de URLs
        self.starships = starships  # Lista de URLs
        self.vehicles = vehicles  # Lista de URLs
        self.species = species  # Lista de URLs
        Film.film_list.append(self)

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Release Date: {self.release_date}"
