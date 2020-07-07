import os

from flask import Flask

from film.lib import log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = log.init_log("film", F"{BASE_DIR}/logs/film")


def create_app():
    app = Flask(__name__)
    from film.modules import api_blu
    app.register_blueprint(api_blu)
    return app
