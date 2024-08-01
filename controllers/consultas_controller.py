from flask import render_template, make_response
from flask_restful import Resource # type: ignore
from models.ventas import Ventas
from models.ingredientes import Ingredientes
from models.sabores import Sabores
from models. productos import Productos
from db import db
from sqlalchemy import text # type: ignore
from flask_login import login_required
from auth import role_required


class VentasController(Resource):
    
    @role_required([1])
    def get(self):
        
        ventas = Ventas.query.all()
        
        return make_response(render_template("ventas.html", ventas=ventas))
    
    
    
class CaloriasController(Resource):
    
    @role_required([1,2,3])
    def get(self):
        
        ventas = Ventas.query.order_by(Ventas.producto).all()
        
        return make_response(render_template("calorias.html", ventas=ventas))
    
    
    
class IngredientesController(Resource):
    
    @role_required([1,2])
    @login_required
    def get(self):
        ingredientes = Ingredientes.query.order_by(Ingredientes.idIngrediente).all()
        return make_response(render_template("ingredientes.html",ingredientes=ingredientes))
    
    
class ProductosController(Resource):
    
    def get(self):
        productos = Productos.query.all()
        return make_response(render_template("index.html",productos=productos))
    