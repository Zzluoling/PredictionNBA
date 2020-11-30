from flask_login import LoginManager
from .User import login_manager

def init_app(app):
    login_manager.init_app(app)