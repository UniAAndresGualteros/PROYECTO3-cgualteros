from datetime import datetime
from db import db
import pytz # type: ignore

def hora_bogota():
    bogota_hora = pytz.timezone('America/Bogota')
    return datetime.now(bogota_hora)


class Ventas(db.Model):
    idVenta = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.DateTime, default=hora_bogota)
    producto = db.Column(db.Integer, db.ForeignKey('productos.idProducto'), nullable=False)
    ingrediente_1 = db.Column(db.Integer, db.ForeignKey('ingredientes.idIngrediente'), nullable=False)
    ingrediente_2 = db.Column(db.Integer, nullable=False)
    ingrediente_3 = db.Column(db.Integer, nullable=False)
    precio_base = db.Column(db.Float, nullable=False)
    precio_plastico = db.Column(db.Float, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    
    productos = db.relationship('Productos', backref='ventas',lazy=True)
    ingredientes = db.relationship('Ingredientes', backref='ventas',lazy=True)
    
    
    