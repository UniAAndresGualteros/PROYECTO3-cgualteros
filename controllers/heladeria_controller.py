from flask import render_template, make_response, request, redirect, url_for, flash
from flask_restful import Resource # type: ignore
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.sabores import Sabores
from models.ventas import Ventas
from models.funciones import *
from db import db


class HeladeriaController(Resource):
    
    def get(self):
        ingredientes = Ingredientes.query.join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).order_by(Ingredientes.idIngrediente).all()
        productos = Productos.query.all()
        return make_response(render_template("index.html",ingredientes=ingredientes, productos=productos))
     
    
class HeladosVender(Resource):
    def post(self):
        selected_ingredientes = request.form.getlist('ingredientes')
        selected_producto = request.form.get('producto')

        if not selected_producto or len(selected_ingredientes) != 3 :
            flash("Error: Debe seleccionar un producto y tres ingredientes.")
            return redirect(url_for('heladeriacontroller'))
        
        producto = Productos.query.get(selected_producto)
        precioBase = 0
        inventario_suficiente = True
        ingredientes_info = []
        precio_plastico = 0

        if producto.tipo_producto == "Malteada":
            precio_plastico = 500

        for ingrediente_id in selected_ingredientes:
            if ingrediente_id:
                ingrediente = Ingredientes.query.get(ingrediente_id)
                if ingrediente.tipo_ingrediente == "Base" and ingrediente.inventario < 1:
                    flash(f"Error: No hay suficiente inventario para el ingrediente {ingrediente.nombre}.")
                    inventario_suficiente = False
                    break
                elif ingrediente.tipo_ingrediente == "Complemento" and ingrediente.inventario < 0.2:
                    flash(f"Error: No hay suficiente inventario para el complemento {ingrediente.nombre}.")
                    inventario_suficiente = False
                    break
                precioBase += ingrediente.precio
                ingredientes_info.append(ingrediente)

        if not inventario_suficiente:
            return redirect(url_for('heladeriacontroller'))

        precio_total = precio_plastico + precioBase
        precioPublico = producto.precio_publico

        nueva_venta = Ventas(
            producto=selected_producto,
            ingrediente_1=selected_ingredientes[0],
            ingrediente_2=selected_ingredientes[1],
            ingrediente_3=selected_ingredientes[2],
            precio_base = precioBase,
            precio_plastico = precio_plastico,
            precio_total =precio_total,
            precio_publico= precioPublico
        )

        try:
            db.session.add(nueva_venta)
            db.session.commit()

            # Actualizar inventario
            for ingrediente in ingredientes_info:
                if ingrediente.tipo_ingrediente == "Base":
                    ingrediente.inventario -= 1
                elif ingrediente.tipo_ingrediente == "Complemento":
                    ingrediente.inventario -= 0.2
                db.session.add(ingrediente)
            db.session.commit()

            flash("Venta registrada con éxito.")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al guardar la venta: {e}")

        return redirect(url_for('heladeriacontroller'))