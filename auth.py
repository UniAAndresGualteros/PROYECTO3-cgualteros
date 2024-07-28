from flask import jsonify, request
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from functools import wraps
from models.usuarios import Usuarios

login_manager = LoginManager()
login_manager.login_view = 'login'

def role_required(required_roles):
    def wrapper(fn):
        @wraps(fn)
        @login_required
        def decorated_view(*args, **kwargs):
            if current_user.rol_usuario not in required_roles:
                response = jsonify({'error': 'Acceso No Autorizado'})
                response.status_code = 401
                return response
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

def init_login(app):
    login_manager.init_app(app)