from json import loads, dumps
from resources.databaseSeries import Serie


class EpisodesModel:

    def __init__(self, title, synopsis, season, episodes_id):

        self.title = title
        self.synopsis = synopsis
        self.season = season
        self.episodes_id = episodes_id

    @classmethod
    def list_to_dict(cls):
        return loads(dumps(default=EpisodesModel.to_dict))

    def to_dict(self):
        serie = Serie.query.filter_by(id=self.episodes_id).first()
        return {
            "Title Episode": self.title,
            "Synopsis": self.synopsis,
            "season": self.season,
            "Serie Name": serie.title
            }