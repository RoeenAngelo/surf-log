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
        return f"Date: {self.date} | Time: {self.time} | Wave Height: {self.wave_height} | Wind: {self.wind} | Tide: {self.tide} | Crowd: {self.crowd} | UV: {self.uv} | Board: {self.board} | Fins: {self.fins} | Duration: {self.duration} | Rating: {self.rating} | Notes: {self.notes}"