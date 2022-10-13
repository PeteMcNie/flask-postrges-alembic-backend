from flask import Flask

import model as m
from app.blueprints.example import example
from app.blueprints.test import test

app = Flask(__name__)
app.config.from_object("app.settings.default")
app.config.from_envvar("APP_SETTINGS")

# Set up a direnv file in backend to automatcially set environment variables

m.db.init_app(app)

app.register_blueprint(test)

# app.register_blueprint(example) Keep adding each blueprint file here
