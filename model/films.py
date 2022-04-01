from json import loads, dumps


class FilmModel:

    def __init__(self, title, synopsis, genre, evaluation, launch):

        self.title = title
        self.synopsis = synopsis
        self.genre = genre
        self.evaluation = evaluation
        self.launch = launch

    @classmethod
    def list_to_dict(cls):
        return loads(dumps(default=FilmModel.to_dict))

    def to_dict(self):
        return {
            "Title": self.title,
            "Synopsis": self.synopsis,
            "Genre": self.genre,
            "Evaluation": self.evaluation,
            "Launch": self.launch
        }
