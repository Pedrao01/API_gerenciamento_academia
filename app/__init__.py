from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    Migrate(app, db)

    from app import models

    # Blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/user')

    return app
