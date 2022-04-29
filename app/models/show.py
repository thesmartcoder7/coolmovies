class Show:
    def __init__(self, id, name, overview, poster):
        self.id = id
        self.name = name
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
