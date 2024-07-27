from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import LoginManager


db = SQLAlchemy()

login_manager = LoginManager()
