from datetime import datetime
from db import db
import pytz # type: ignore

def hora_bogota():
    bogota_hora = pytz.timezone('America/Bogota')
    return datetime.now(bogota_hora)


class Ventas(db.Model):
    idventa = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.DateTime, default=hora_bogota)
    producto = db.Column(db.Integer, db.ForeignKey('productos.idproducto'), nullable=False)
    ingrediente_1 = db.Column(db.Integer, db.ForeignKey('ingredientes.idingrediente'), nullable=False)
    ingrediente_2 = db.Column(db.Integer, db.ForeignKey('ingredientes.idingrediente'), nullable=False)
    ingrediente_3 = db.Column(db.Integer, db.ForeignKey('ingredientes.idingrediente'), nullable=False)
    precio_base = db.Column(db.Float, nullable=False)
    precio_plastico = db.Column(db.Float, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    
    productos = db.relationship('Productos', backref='ventas',lazy=True)
    ingrediente1 = db.relationship('Ingredientes',foreign_keys=[ingrediente_1],backref='Ventas1')
    ingrediente2 = db.relationship('Ingredientes',foreign_keys=[ingrediente_2],backref='Ventas2')
    ingrediente3 = db.relationship('Ingredientes',foreign_keys=[ingrediente_3],backref='Ventas3')
 

    def ContarCalorias(self):
        
        if self.productos.tipo_producto == "Copa":
            calorias = round((self.ingrediente1.calorias + self.ingrediente2.calorias + self.ingrediente3.calorias) * 0.95, 2)
            
            
        elif self.productos.tipo_producto == "Malteada":
            calorias = round((self.ingrediente1.calorias + self.ingrediente2.calorias + self.ingrediente3.calorias) + 200, 2)
            
            
        return calorias
            
        
          
    
    