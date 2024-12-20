from flask import Flask
from .db import db, migrate
from app.models.planet import Planet
from .routes.planet_routes import planets_bp
import os

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if test_config:
        app.config.update(test_config)


    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)

    return app
