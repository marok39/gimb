import csv
from pprint import PrettyPrinter

class Movie:
    def __init__(self, data):
        self.year = int(data[0]) if data[0] else None
        self.title = data[1].rstrip()
        self.rating = float(data[2]) if data[2] else None
        self.votes = int(data[3]) if data[3] else None

    def __str__(self):
        return str((self.title, self.votes, self.year, self.rating))

    def __repr__(self):
        return str(self)


def read_file(path):
    data = []
    with open(path, "r") as f:
        for line in csv.reader(f):
            data.append(line)
    return data

def find_best_rated(movies):
    if movies:
        best_rated = movies[0]
        for movie in movies[1:]:
            if movie.rating > best_rated.rating:
                best_rated = movie
        return best_rated
    return None

def filter_by_year(movies, year):
    return [m for m in movies if m.year == year]

def find_best_rated_by_year(movies, year):
    return find_best_rated(filter_by_year(movies, year))

def filter_by_rating_or_votes(movies, min_rating=0, votes=0):
    return [m for m in movies if m.rating >= min_rating and m.votes >= votes]

def avg_rating(movies):
    return sum([m.rating for m in movies]) / len(movies)

def main():
    data = read_file("test-2/data/imdb_movie_database.csv")
    pp = PrettyPrinter(indent=2)

    movies = []
    for line in data[1:]:
        m = Movie(line)
        movies.append(m)

    pp.pprint(find_best_rated(movies))
    pp.pprint(find_best_rated_by_year(movies, 207))
    pp.pprint(filter_by_rating_or_votes(movies, min_rating=9.0, votes=10000))
    pp.pprint(avg_rating(movies))

if __name__ == "__main__":
    main()
