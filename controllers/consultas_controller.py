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
        sql_query = text("""
        select V.fecha_venta, P.nombre as Producto, P.tipo_producto, concat(I1.nombre,' ',S1.nombre) Ingrediente1, I1.precio as Precio_1, I1.tipo_ingrediente as Tipo_1,
        concat(I2.nombre,' ',S2.nombre) Ingrediente2, I2.precio as Precio_2, I2.tipo_ingrediente as Tipo_2, concat(I3.nombre,' ',S3.nombre) Ingrediente3,
        I3.precio as Precio_3, I3.tipo_ingrediente as Tipo_3, V.precio_base, V.precio_plastico, V.precio_total, V.precio_publico 
        from ventas V inner join productos P on V.producto= P.idProducto 
        inner join ingredientes I1 on V.ingrediente_1 = I1.idIngrediente
        inner join ingredientes I2 on V.ingrediente_2 = I2.idIngrediente
        inner join ingredientes I3 on V.ingrediente_3 = I3.idIngrediente
        inner join sabores S1 on I1.sabor_base = S1.idSabor 
        inner join sabores S2 on I2.sabor_base = S2.idSabor
        inner join sabores S3 on I3.sabor_base = S3.idSabor
        order by V.idVenta;
        """)
        result = db.session.execute(sql_query)
        ventas = result.fetchall()
        return make_response(render_template("ventas.html", ventas=ventas))
    
    
class IngredientesController(Resource):
    
    @role_required([1,2])
    @login_required
    def get(self):
        ingredientes = Ingredientes.query.join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).order_by(Ingredientes.idIngrediente).all()
        return make_response(render_template("ingredientes.html",ingredientes=ingredientes))
    
    
class ProductosController(Resource):
    
    def get(self):
        productos = Productos.query.all()
        return make_response(render_template("index.html",productos=productos))
    