from model import app, database
from model.episodes import EpisodesModel
from resources.databaseEpisodes import Episodes
from flask import abort, jsonify, request
from resources.validate import *


@app.route('/episode/<int:episodes_id>', methods=['GET'])
def get_episodes_by_serie(episodes_id):
    episodes = Episodes.query.filter_by(episodes_id=episodes_id).all()
    if episodes:
        return jsonify(episodes)
    else:
        abort(400, description="Movies not found")


@app.route('/episode/season/<string:season>', methods=['GET'])
def get_episodes_by_season(season):
    episodes = Episodes.query.filter_by(season_episode=season).all()
    if episodes:
        return jsonify(episodes)
    else:
        abort(400, description="Episodes not found")


@app.route('/episode/title/<string:title>', methods=['GET'])
def get_episode_by_title(title):
    episode = Episodes.query.filter_by(title_episode=title).first()
    if episode:
        return jsonify(episode)
    else:
        abort(400, description="Title not found")


@app.route('/episode/<int:number_episode>', methods=['DELETE'])
def delete_episode(number_episode):
    episode_delete = Episodes.query.get(number_episode)
    if episode_delete:
        database.session.delete(episode_delete)
        database.session.commit()
        return jsonify(episode_delete)
    else:
        abort(400, description="Id not found")


@app.route('/episode/<int:number_episode>', methods=['PUT'])
def put_episode(number_episode):
    episode_update = Episodes.query.get(number_episode)
    if episode_update:
        body = request.get_json()

        validate_title(body['title'])
        validate_synopsis(body['synopsis'])
        validate_seasons(body['season'])
        validate_episodesid(body['episodes_id'])

        episode_update.title_episode = body['title']
        episode_update.synopsis_episode = body['synopsis']
        episode_update.season_episode = body['season']
        episode_update.episodes_id = body['episodes_id']

        database.session.commit()
        return jsonify(episode_update)
    else:
       abort(400, description="Id not found")


@app.route('/episode', methods=['POST'])
def create_episode():
    body = request.get_json()
    new_episode = EpisodesModel(
        body["title"], body["synopsis"], body["season"], body["episodes_id"])

    validate_title(new_episode.title)
    validate_synopsis(new_episode.synopsis)
    validate_seasons(new_episode.season)
    validate_episodesid(new_episode.episodes_id)

    episode = Episodes(title_episode=new_episode.title, synopsis_episode=new_episode.synopsis,
                       season_episode=new_episode.season, episodes_id=new_episode.episodes_id)
    database.session.add(episode)
    database.session.commit()

    return jsonify(new_episode.to_dict())
