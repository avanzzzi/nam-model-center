"""
    :author Gabriel Avanzi
    :license: MIT
"""
import os

import click
from flask import Flask

from nmc.blueprints.auth import auth_bp
from nmc.models import db
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

    db.init_app(app)

    app.register_blueprint(auth_bp)

    register_commands(app)

    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')
