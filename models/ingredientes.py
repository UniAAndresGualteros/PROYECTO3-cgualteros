from db import db
from models.sabores import Sabores

class Ingredientes(db.Model):
    idIngrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo_ingrediente = db.Column(db.String(15), nullable=False)
    sabor_base = db.Column(db.Integer, db.ForeignKey('sabores.idSabor'), nullable=False)
    
    sabores = db.relationship('Sabores', backref='ingredientes',lazy=True)
    
    
    def es_sano(idIngrediente) -> bool:
        ingrediente = Ingredientes.query.get(idIngrediente)
        
        if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
            return True
        return False
        
    
    def abastecer(idIngrediente):
        ingrediente = Ingredientes.query.filter(Ingredientes.idIngrediente == idIngrediente).first()
    
        if ingrediente:
            if ingrediente.tipo_ingrediente == 'Base':
                ingrediente.inventario += 5
            elif ingrediente.tipo_ingrediente == 'Complemento':
                ingrediente.inventario += 10
            else:
                raise ValueError("Tipo de ingrediente desconocido")
            db.session.commit()
            return ingrediente
        else:
            raise ValueError("Ingrediente no encontrado")
    
    
    def renovar_inventario(idIngrediente):
        ingrediente = Ingredientes.query.get(idIngrediente)
        if ingrediente.tipo_ingrediente =='Complemento':
            ingrediente.inventario = 0
            mensaje = f"Inventario Renovado"
        else:
            mensaje = f"Ingrediente no es complemento"
            
        db.session.commit()
        return mensaje
        
        