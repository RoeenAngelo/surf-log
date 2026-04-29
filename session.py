class Session:
    def __init__(self, date, time, wave_height, wind, tide, crowd, uv, board, fins, duration, rating, notes):  
        self.date = date
        self.time = time
        self.wave_height = wave_height
        self.wind = wind
        self.tide = tide
        self.crowd = crowd
        self.uv = uv
        self.board = board
        self.fins = fins
        self.duration = duration
        self.rating = rating
        self.notes = notes

    def __str__(self):
        divider = '-' * 50
        return (
            f"\n{divider}\n"
            f"Date: {self.date} | Time: {self.time}\n"
            f"Wave Height: {self.wave_height} | Wind: {self.wind}\n" f"Tide: {self.tide} | Crowd: {self.crowd}\n" 
            f"UV: {self.uv} | Board: {self.board}\n" 
            f"Fins: {self.fins} | Duration: {self.duration}\n"
            f"Rating: {self.rating} | Notes: {self.notes}"
            f"\n{divider}\n"
        )
    
    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "wave_height": self.wave_height,
            "wind": self.wind,
            "tide": self.tide,
            "crowd": self.crowd,
            "uv": self.uv,
            "board": self.board,
            "fins": self.fins,
            "duration": self.duration,
            "rating": self.rating,
            "notes": self.notes,
        }