from movie import Movie
from user import User


user = User("Andrew")

my_movie = Movie("Matrix", "Sci-Fi", False)
user.movies.append(my_movie)

print(user)
print(user.watched_movies())


