from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# Initialize dictionary
movies = {
    'Action': [
        {'Title': 'The Dark Knight', 'Year': 2008, 'Director': 'Christopher Nolan', 'Rating': 9.0},
        {'Title': 'Inception', 'Year': 2010, 'Director': 'Christopher Nolan', 'Rating': 8.8},
        {'Title': 'The Matrix', 'Year': 1999, 'Director': 'Lana, Lilly Wachowski', 'Rating': 8.7},
        {'Title': 'The Gladiator', 'Year': 2000, 'Director': 'Ridley Scott', 'Rating': 8.5},
        {'Title': 'Raiders of the Lost Ark', 'Year': 1981, 'Director': 'Steven Spielberg', 'Rating': 8.4}
    ],
    'Adventure': [
        {'Title': 'Interstellar', 'Year': 2014, 'Director': 'Christopher Nolan', 'Rating': 8.7},
        {'Title': 'Back to the Future', 'Year': 1985, 'Director': 'Robert Zemeckis', 'Rating': 8.5},
        {'Title': 'Harry Potter and the Prisoner of Azkaban', 'Year': 2004, 'Director': 'Alfonso Cuarón', 'Rating': 8.0},
        {'Title': 'Cast Away', 'Year': 2000, 'Director': 'Robert Zemeckis', 'Rating': 7.8},
        {'Title': 'Star Trek', 'Year': 2009, 'Director': 'J.J. Abrams', 'Rating': 7.9}
    ],
    'Animation': [
        {'Title': 'WALL•E', 'Year': 2008, 'Director': 'Andrew Stanton', 'Rating': 8.4},
        {'Title': 'Spirited Away', 'Year': 2001, 'Director': 'Hayao Miyazaki', 'Rating': 8.6},
        {'Title': 'The Lion King', 'Year': 1994, 'Director': 'Roger Allers, Rob Minkoff', 'Rating': 8.5},
        {'Title': 'Finding Nemo', 'Year': 2003, 'Director': 'Andrew Stanton, Lee Unkrich', 'Rating': 8.2},
        {'Title': 'Toy Story', 'Year': 1995, 'Director': 'John Lasseter', 'Rating': 8.3}
    ],
    'Comedy': [
        {'Title': 'Django Unchained', 'Year': 2012, 'Director': 'Quentin Tarantino', 'Rating': 8.5},
        {'Title': 'The Truman Show', 'Year': 1998, 'Director': 'Peter Weir', 'Rating': 8.2},
        {'Title': 'Knives Out', 'Year': 2019, 'Director': 'Rian Johnson', 'Rating': 7.9},
        {'Title': 'Groundhog Day', 'Year': 1993, 'Director': 'Harold Ramis', 'Rating': 8.0},
        {'Title': 'Home Alone', 'Year': 1990, 'Director': 'Chris Columbus', 'Rating': 7.7}
    ],
    'Drama': [
        {'Title': 'The Shawshank Redemption', 'Year': 1994, 'Director': 'Frank Darabont', 'Rating': 9.3},
        {'Title': 'Forrest Gump', 'Year': 1994, 'Director': 'Robert Zemeckis', 'Rating': 8.8},
        {'Title': 'Pulp Fiction', 'Year': 1994, 'Director': 'Quentin Tarantino', 'Rating': 8.9},
        {'Title': 'The Godfather', 'Year': 1972, 'Director': 'Francis Ford Coppola', 'Rating': 9.2},
        {'Title': 'The Departed', 'Year': 2006, 'Director': 'Martin Scorsese', 'Rating': 8.5}
    ],
    'Horror': [
        {'Title': 'The Silence of the Lambs', 'Year': 1991, 'Director': 'Jonathan Demme', 'Rating': 8.6},
        {'Title': 'The Shining', 'Year': 1980, 'Director': 'Stanley Kubrick', 'Rating': 8.4},
        {'Title': 'Alien', 'Year': 1979, 'Director': 'Ridley Scott', 'Rating': 8.5},
        {'Title': 'Get Out', 'Year': 2017, 'Director': 'Jordan Peele', 'Rating': 7.8},
        {'Title': 'It', 'Year': 2017, 'Director': 'Andy Muschietti', 'Rating': 7.3}
    ],
    'Musical': [
        {'Title': 'La La Land', 'Year': 2016, 'Director': 'Damien Chazelle', 'Rating': 8.0},
        {'Title': 'Frozen', 'Year': 2013, 'Director': 'Chris Buck, Jennifer Lee', 'Rating': 7.4},
        {'Title': 'The Wizard of Oz', 'Year': 1939, 'Director': 'Victor Fleming, King Vidor', 'Rating': 8.1},
        {'Title': 'The Greatest Showman', 'Year': 2017, 'Director': 'Michael Gracey', 'Rating': 7.5},
        {'Title': 'Mamma Mia!', 'Year': 2008, 'Director': 'Phyllida Lloyd', 'Rating': 6.5},
    ],
    'Romance': [
        {'Title': 'Titanic', 'Year': 1997, 'Director': 'James Cameron', 'Rating': 7.9},
        {'Title': 'Life is Beautiful', 'Year': 1997, 'Director': 'Roberto Benigni', 'Rating': 8.6},
        {'Title': 'The Notebook', 'Year': 2004, 'Director': 'Nick Cassavetes', 'Rating': 7.8},
        {'Title': 'A Star is Born', 'Year': 2018, 'Director': 'Bradley Cooper', 'Rating': 7.6},
        {'Title': 'Pearl Harbor', 'Year': 2001, 'Director': 'Michael Bay', 'Rating': 6.2}
    ],
    'Thriller': [
        {'Title': 'Se7en', 'Year': 1995, 'Director': 'David Fincher', 'Rating': 8.6},
        {'Title': 'Shutter Island', 'Year': 2010, 'Director': 'Martin Scorsese', 'Rating': 8.2},
        {'Title': 'Memento', 'Year': 2000, 'Director': 'Christopher Nolan', 'Rating': 8.4},
        {'Title': 'Mad Max: Fury Road', 'Year': 2015, 'Director': 'George Miller', 'Rating': 8.1},
        {'Title': 'The Sixth Sense', 'Year': 1999, 'Director': 'M. Night Shyamalan', 'Rating': 8.2}
    ],
}

@app.route('/')
def index():
    return render_template('index.html', genres=movies.keys())

@app.route('/movies/<genre>')
def movie_recommendations(genre):
    if genre in movies:
        return render_template('recommendations.html', genre=genre, movies=movies[genre])
    else:
        return "Genre not found", 404

if __name__ == '__main__':
    app.run(debug=True)
