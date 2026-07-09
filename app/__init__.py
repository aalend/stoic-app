from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.routes.main import main
from config import Config

# Init db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load all settings from class Config
    app.config.from_object(Config)

    # Register blueprint form routes/main
    app.register_blueprint(main)

    # Connect db with Flask app
    db.init_app(app)

    with app.app_context():
        from app.models import Entry, StoicCard, Theme, User

        db.create_all()
    return app
