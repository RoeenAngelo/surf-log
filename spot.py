class Spot:
    def __init__(self, name, location, difficulty):
        self.name = name
        self.location = location
        self.difficulty = difficulty

    def __str__(self):
        return f"Spot: {self.name} | Location: {self.location} | Difficulty: {self.difficulty}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "location" : self.location,
            "difficulty" : self.difficulty,
        }