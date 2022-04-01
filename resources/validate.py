from flask import abort


def validate_title(title):
    validate_type = isinstance(title, int) or isinstance(title, float)
    if validate_type:
        abort(400, description="The title field only accepts the string type")


def validate_seasons(seasons):

    validate_type = isinstance(seasons, float) or type(seasons) == str
    if validate_type:
        abort(400, description="The seasons field only accepts the integer type")

    validate_value = seasons < 1
    if validate_value:
        abort(400, description="The seasons field only accepts values greater than 1")


def validate_evaluation(evaluation):

    validate_type = isinstance(evaluation, float) or type(evaluation) == str
    if validate_type:
        abort(400, description="The evaluation field only accepts the integer type")

    validate_value = (evaluation > 5) or (evaluation < 1)
    if validate_value:
        abort(400, description="The evaluation field must be between 1 and 5")


def validate_synopsis(synopsis):
    validate_type = isinstance(synopsis, int) or isinstance(synopsis, float)
    if validate_type:
        abort(400, description="The synopsis field only accepts the string type")


def validate_genre(genre):
    validate_type = isinstance(genre, int) or isinstance(genre, float)
    if validate_type:
        abort(400, description="The genre field only accepts the string type")


def validate_launch_film(launch_film):

    validate_type = isinstance(launch_film, float) or type(launch_film) == str
    if validate_type:
        abort(400, description="The launch field only accepts the integer type")

    validate_year = launch_film < 1888
    if validate_year:
        abort(400, description="The launch field only accepts values greater than 1888")


def validate_episodesid(episodes_id):

    validate_type = isinstance(
        episodes_id, float) or type(episodes_id) == str
    if validate_type:
        abort(400, description="The episode ID field only accepts the integer type")

    validate_value = episodes_id < 1
    if validate_value:
        abort(400, description="The episode ID field only accepts values greater than 1")
