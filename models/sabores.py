from db import db

class Sabores(db.Model):
    idsabor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    
    
    