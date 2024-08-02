from db import db

class Roles(db.Model):
    idrol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(20), nullable=False)