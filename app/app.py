from flask import Flask

import model as m
from app.blueprints.example import example
from app.blueprints.test import test_get_all

app = Flask(__name__)
app.config.from_object("app.settings.default")
app.config.from_envvar("FLASK_APP")
# app.config.from_envvar("APP_SETTINGS")

m.db.init_app(app)

app.register_blueprint(example)
app.register_blueprint(test_get_all)

# app.register_blueprint(example) Keep adding each blueprint file here
