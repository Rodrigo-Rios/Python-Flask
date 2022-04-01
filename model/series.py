from json import loads, dumps


class SeriesModel:

    def __init__(self, title, synopsis, genre, evaluation, seasons):

        self.title = title
        self.synopsis = synopsis
        self.genre = genre
        self.evaluation = evaluation
        self.seasons = seasons

    @classmethod
    def list_to_dict(cls):
        return loads(dumps(default=SeriesModel.to_dict))

    def to_dict(self):
        return {
            "Title": self.title,
            "Synopsis": self.synopsis,
            "Genre": self.genre,
            "Evaluation": self.evaluation,
            "Seasons": self.seasons
        }
