from db import db

class Productos(db.Model):
    idProducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo_producto = db.Column(db.String(80), nullable=False)
    presentacion = db.Column(db.String(80), nullable=False)
    
    
    def consultarProductos(self):
        return f"Id Producto: {self.idProducto} Nombre: {self.nombre}"
    
    