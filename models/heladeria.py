from models.ingredientes import Ingredientes
from models.productos import Productos
from models.sabores import Sabores

class Heladeria():
    def __init__(self):
        self.ingredientes = Ingredientes.query.join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).all()
        self.productos = Productos.query.all()
        
        
    def mostar_productos(self):
        return self.productos
    
    def mostrar_ingredientes(self):
        return self.ingredientes
    
    def __repr__(self):
        return self.mostar_productos()