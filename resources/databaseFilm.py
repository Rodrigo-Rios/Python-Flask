from model import database
from dataclasses import dataclass


@dataclass
class FilmDb(database.Model):

    id_film: int
    title_film: str
    synopsis_film: str
    genre_film: str
    evaluation_film: int
    launch_film: int

    id_film = database.Column(database.Integer, primary_key=True)
    title_film = database.Column(database.String, nullable=False)
    synopsis_film = database.Column(database.Text, nullable=False)
    genre_film = database.Column(database.String, nullable=False)
    evaluation_film = database.Column(database.Integer, nullable=False)
    launch_film = database.Column(database.Integer, nullable=False)
