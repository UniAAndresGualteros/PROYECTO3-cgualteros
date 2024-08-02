from db import db

class Productos(db.Model):
    idproducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo_producto = db.Column(db.String(80), nullable=False)
    presentacion = db.Column(db.String(80), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    
    
    def consultarProductos(self):
        return f"Id Producto: {self.idproducto} Nombre: {self.nombre}"
    
    