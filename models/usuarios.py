from flask_login import UserMixin # type: ignore
from db import db

class Usuarios(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    rol_usuario = db.Column(db.Integer, db.ForeignKey('roles.idrol'), nullable=False)
    
    roles = db.relationship('Roles', backref='Usuarios',lazy=True)
    
    def __init__(self,id:int, username:str, password:str, rol_usuario:int):
        self.id = id
        self.username = username
        self.password = password
        self.rol_usuario = rol_usuario
        
    def __repr__(self):
        return f'<User {self.username}>'