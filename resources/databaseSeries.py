from model import database
from dataclasses import dataclass


@dataclass
class Serie(database.Model):

    id: int
    title: str
    synopsis: str
    genre: str
    evaluation: int
    seasons: int

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    synopsis = database.Column(database.Text, nullable=False)
    genre = database.Column(database.String, nullable=False)
    evaluation = database.Column(database.Integer, nullable=False)
    seasons = database.Column(database.Integer, nullable=False)
    episodes = database.relationship('Episodes', backref='episodes')
