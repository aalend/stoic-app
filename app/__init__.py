from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Init db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load all settings from class Config
    app.config.from_object(Config)

    # Connect db with Flask app
    db.init_app(app)

    with app.app_context():
        from app.models import Entry, StoicCard, Theme, User

        db.create_all()

    # Register blueprint form routes/
    from app.routes.auth import auth
    from app.routes.main import main

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
