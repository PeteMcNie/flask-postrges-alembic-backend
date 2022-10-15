from flask import Flask

import model as m
from app.blueprints.test import test

app = Flask(__name__)
app.config.from_object("app.settings.default")
app.config.from_envvar("APP_SETTINGS")

m.db.init_app(app)

app.register_blueprint(test)
