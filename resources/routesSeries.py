from model import app, database
from model.series import SeriesModel
from resources.databaseSeries import Serie
from resources.databaseEpisodes import Episodes
from flask import abort, jsonify, request
from resources.validate import *


@app.route('/serie/episodes/<string:title>', methods=['GET'])
def get_all_episodes_by_serie(title):
    series = Serie.query.filter_by(title=title).first()
    episodes = Episodes.query.filter_by(episodes_id=series.id).all()
    if episodes:
        return jsonify(episodes)
    else:
        abort(400, description="Series not found")


@app.route('/serie', methods=['GET'])
def get_all_series():
    series = Serie.query.all()
    if series:
        return jsonify(series)
    else:
        abort(400, description="Series not found")


@app.route('/serie/<int:id>', methods=['GET'])
def get_id_serie(id):
    series = Serie.query.get(id)
    if series:
        return jsonify(series)
    else:
        abort(400, description="Id not found")


@app.route('/serie/genre/<string:genre>', methods=['GET'])
def get_genre_serie(genre):
    series = Serie.query.filter_by(genre=genre).all()
    if series:
        return jsonify(series)
    else:
        abort(400, description="Genre not found")


@app.route('/serie/title/<string:title>', methods=['GET'])
def get_title_serie(title):
    series = Serie.query.filter_by(title=title).all()
    if series:
        return jsonify(series)
    else:
        abort(400, description="Title not found")


@app.route('/serie/<int:id>', methods=['DELETE'])
def delete_serie(id):
    serie_delete = Serie.query.get(id)
    if serie_delete:
        database.session.delete(serie_delete)
        database.session.commit()
        return jsonify(serie_delete)
    else:
        abort(400, description="Id not found")


@app.route('/serie/<int:id>', methods=['PUT'])
def put_serie(id):
    serie_update = Serie.query.get(id)
    if serie_update:
        body = request.get_json()

        validate_title(body['title'])
        validate_synopsis(body['synopsis'])
        validate_genre(body['genre'])
        validate_evaluation(body['evaluation'])
        validate_seasons(body['seasons'])

        serie_update.title = body['title']
        serie_update.synopsis = body['synopsis']
        serie_update.genre = body['genre']
        serie_update.evaluation = body['evaluation']
        serie_update.seasons = body['seasons']

        database.session.commit()
        return jsonify(serie_update)
    else:
       abort(400, description="Id not found")


@app.route('/serie', methods=['POST'])
def create_serie():
    body = request.get_json()
    new_serie = SeriesModel(body["title"], body["synopsis"],
                            body["genre"], body["evaluation"], body["seasons"])

    validate_title(new_serie.title)
    validate_synopsis(new_serie.synopsis)
    validate_genre(new_serie.genre)
    validate_evaluation(new_serie.evaluation)
    validate_seasons(new_serie.seasons)

    serie = Serie(title=new_serie.title, synopsis=new_serie.synopsis, genre=new_serie.genre, evaluation=new_serie.evaluation,
                  seasons=new_serie.seasons)
    database.session.add(serie)
    database.session.commit()

    return jsonify(new_serie.to_dict())
