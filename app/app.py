from flask import Flask
from flask_cors import CORS

import model as m
from app.blueprints.example import example

app = Flask(__name__)
CORS(app)
app.config.from_object("app.settings.default")
app.config.from_envvar("APP_SETTINGS")

m.db.init_app(app)

app.register_blueprint(example)
