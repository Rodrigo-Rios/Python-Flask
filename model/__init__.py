from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///catalog.db"

database = SQLAlchemy(app)


from resources import routesFilms
from resources import routesEpisodes
from resources import routesSeries

if database:
    database.create_all()
