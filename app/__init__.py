from flask import Flask, session, g
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    Migrate(app, db)

    from app.models.user import User

    @app.before_request
    def load_logged_user():
        user_id = session.get('user_id')
        if user_id is None:
            g.user = None
        else:
            g.user = User.query.get(user_id)

    # Blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/user')

    from app.routes.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/user')

    return app
