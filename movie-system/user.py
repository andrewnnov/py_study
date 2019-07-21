class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)
    
    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))




