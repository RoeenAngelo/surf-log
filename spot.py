class Spot:
    def __init__(self, name, location, difficulty):
        self.name = name
        self.location = location
        self.difficulty = difficulty

    def __str__(self):
        divider = '-' * 50
        return (
            f"\n{divider}\n"
            f"Spot: {self.name}\n"
            f"Location: {self.location}\n" 
            f"Difficulty: {self.difficulty}"
            f"\n{divider}\n"
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "location" : self.location,
            "difficulty" : self.difficulty,
        }
    
    