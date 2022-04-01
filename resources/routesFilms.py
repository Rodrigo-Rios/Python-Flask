from model import app, database
from model.films import FilmModel
from resources.databaseFilm import FilmDb
from flask import abort, jsonify, request
from resources.validate import *


@app.route('/film', methods=['GET'])
def get_all():
    movies = FilmDb.query.all()
    if movies:
        return jsonify(movies)
    else:
        abort(400, description="Movies not found")


@app.route('/film/<int:id_film>', methods=['GET'])
def get_id(id_film):
    movies = FilmDb.query.get(id_film)
    if movies:
        return jsonify(movies)
    else:
        abort(400, description="Id not found")


@app.route('/film/genre/<string:genre_film>', methods=['GET'])
def get_genre(genre_film):
    movies = FilmDb.query.filter_by(genre_film=genre_film).all()
    if movies:
        return jsonify(movies)
    else:
        abort(400, description="Genre not found")


@app.route('/film/synopsis/<string:synopsis_film>', methods=['GET'])
def get_synopsis(synopsis_film):
    movies = FilmDb.query.filter_by(synopsis_film=synopsis_film).all()
    if movies:
        return jsonify(movies)
    else:
        abort(400, description="Name not found")


@app.route('/film/title/<string:title_film>', methods=['GET'])
def get_title(title_film):
    movies = FilmDb.query.filter_by(title_film=title_film).all()
    if movies:
        return jsonify(movies)
    else:
        abort(400, description="Name not found")


@app.route('/film/<int:id_film>', methods=['DELETE'])
def delete(id_film):
    movie_delete = FilmDb.query.get(id_film)
    if movie_delete:
        database.session.delete(movie_delete)
        database.session.commit()
        return jsonify(movie_delete)
    else:
        abort(400, description="Id not found")


@app.route('/film/<int:id_film>', methods=['PUT'])
def put(id_film):
    movie_update = FilmDb.query.get(id_film)
    if movie_update:
        body = request.get_json()

        validate_title(body['title'])
        validate_synopsis(body['synopsis'])
        validate_genre(body['genre'])
        validate_evaluation(body['evaluation'])
        validate_launch_film(body['launch'])

        movie_update.title_film = body['title']
        movie_update.synopsis_film = body['synopsis']
        movie_update.genre_film = body['genre']
        movie_update.evaluation_film = body['evaluation']
        movie_update.launch_film = body['launch']

        database.session.commit()
        return jsonify(movie_update)
    else:
       abort(400, description="Id not found")


@app.route('/film', methods=['POST'])
def create_post():
    body = request.get_json()
    new_movie = FilmModel(body["title"], body["synopsis"],
                          body["genre"], body["evaluation"], body["launch"])

    validate_title(new_movie.title)
    validate_synopsis(new_movie.synopsis)
    validate_genre(new_movie.genre)
    validate_evaluation(new_movie.evaluation)
    validate_launch_film(new_movie.launch)

    movie = FilmDb(title_film=new_movie.title, synopsis_film=new_movie.synopsis, genre_film=new_movie.genre, evaluation_film=new_movie.evaluation,
                   launch_film=new_movie.launch)
    database.session.add(movie)
    database.session.commit()

    return jsonify(new_movie.to_dict())
