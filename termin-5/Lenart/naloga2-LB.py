import csv

class Movie:
    def __init__(self, data):
        self.year = int(data[0]) if data[0] else None
        self.title = data[1].rstrip() if data[1] else None
        self.rating = float(data[2]) if data[2] else None
        self.votes = int(data[3]) if data[3] else None

    def __str__(self):
        return str((self.title, self.votes, self.year, self.rating))

    def __repr__(self):
        return str(self)


def collect_movies(filepath):
    data = []
    movies = []
    with open(filepath, "r") as f:
        next(csv.reader(f))
        for line in csv.reader(f):
            movies.append(Movie(line))
    return movies


def highest_rating(movies, year=None):
    if year:
        movies = [movie for movie in movies if movie.year == year]
    highest = movies[0]
    for movie in movies[1:]:
        if movie.rating > highest.rating:
            highest = movie
    return highest


def better_than(movies, rating=0, amount=0):
    return [movie for movie in movies if movie.votes >= amount and movie.rating >= rating]


def average_rating(movies):
    return sum([movie.rating for movie in movies])/len(movies)


def main():
    movies = collect_movies("imdb_movie_database.csv")
    print(highest_rating(movies, year=int(input("Year: "))))
    print(better_than(movies, rating=float(input("Rating: ")), amount=int(input("Amount: "))))
    print(average_rating(movies))


if __name__ == "__main__":
    main()
