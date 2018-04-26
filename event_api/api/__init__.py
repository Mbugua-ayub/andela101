"""This is the glue"""

from flask import Flask

APP = Flask(__name__)

from event_api.api.auth.views import AUTH
APP.register_blueprint(AUTH)
