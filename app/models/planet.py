class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

planets = [
    Planet(1, "Mercury", "the closest to the Sun", 0),
    Planet(2, "Venus", "similar in size to Earth", 0),
    Planet(3, "Earth", "suitable for live", 1),
    Planet(4, "Mars",  "red", 2),
    Planet(5, "Jupiter", "the largest planet", 95),
    Planet(6, "Saturn","has rings", 146),
    Planet(7, "Uranus", "blue gas giant", 27),
    Planet(8, "Neptune", "dark and cold", 16)

]        
