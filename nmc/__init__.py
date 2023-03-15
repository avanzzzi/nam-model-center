"""
    :author Gabriel Avanzi
    :license: MIT
"""
import os

from flask import Flask

from nmc.blueprints.auth import auth_bp
from nmc.settings import config


def create_app() -> Flask:
    """
    Create configured flask instance

    Returns:
        Configured instance
    """
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    create_app()
