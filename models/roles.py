from db import db

class Roles(db.Model):
    idRol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(20), nullable=False)