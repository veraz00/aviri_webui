from flask import Flask
import sys
import click
import os 
# sys.path.append("..")  
# all the folder, on the same dir, or sub; all use this path as cwd
from flask_migrate import Migrate
from flask_login import current_user
# from app.models import Images, Predictions

from app.extensions import bootstrap, db, login_manager

def register_extensions(app):

    bootstrap.init_app(app)  # bootstrap??
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)


def register_blueprints(app):
    from app.views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.views.image_up import image_up
    app.register_blueprint(image_up, url_prefix='/image_up')


def register_commands(app):  
    @app.cli.command()
    @click.option('--username', prompt = True, help ='username to login in')
    @click.option('--password', prompt = True, hide_input = True, confirmation_prompt = True, help = 'password to login in')
    def init(username, password):  # use flask init to add 
        # ihpc
        # ihpc

        click.echo('Initializing the database...')
        from app.models import Admin
        admin = Admin.query.filter_by(username = username).first()
        if admin != None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username,
                master='Anything about you.',
                about='Anything about you.'
            )
            admin.set_password(password)
        print(username, password)
        db.session.add(admin)
        db.session.commit()

def create_app(config_name = 'develop'):
    app = Flask(__name__)
    
    from config import config_map
    app.config.from_object(config_map[config_name])
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    from app import models 
    
    return app
