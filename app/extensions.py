
import os 

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth_bp/login'  # for tempaltes
login_manager.login_message  = 'login_manager.login_message!'
@login_manager.user_loader
def load_user(user_id):
    from app.models import Admin
    user = Admin.query.get(int(user_id))
    return user
