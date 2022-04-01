from model import database
from dataclasses import dataclass


@dataclass
class Episodes(database.Model):

    number_episode: int
    title_episode: str
    synopsis_episode: str
    season_episode: int
    episodes_id: int

    number_episode = database.Column(
        database.Integer, nullable=False, primary_key=True)
    title_episode = database.Column(database.String, nullable=False)
    synopsis_episode = database.Column(database.Text, nullable=False)
    season_episode = database.Column(database.Integer, nullable=False)
    episodes_id = database.Column(
        database.Integer, database.ForeignKey('serie.id'))
