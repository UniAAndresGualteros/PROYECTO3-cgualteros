from flask import Flask, jsonify, render_template, request
from flask_restful import Resource
from models.productos import Productos
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.ventas import Ventas
from db import db
import random


class ProductosList(Resource):
    def get(self):
        productos = Productos.query.all()
        return jsonify([{
            'idProducto': prod.idProducto,
            'nombre': prod.nombre,
            'Tipo Producto': prod.tipo_producto,
            'Presentacion': prod.presentacion
        } for prod in productos])
        
class ProductoporID(Resource):
    def get(self, id):
        producto = Productos.query.get_or_404(id)
        return jsonify({
            'idProducto': producto.idProducto,
            'nombre': producto.nombre,
            'Tipo Producto': producto.tipo_producto,
            'Presentacion': producto.presentacion
        })
        
        
class ProductoporNombre(Resource):
    def get(self):
        nombre = request.args.get('nombre', None)
        if nombre is None:
            return jsonify({'error': 'Debe proporcionar un nombre de ingrediente'}), 400

        productos = Productos.query.filter(Productos.nombre.like(f"%{nombre}%")).all()
        if not productos:
            return jsonify({'message': 'No se encontraron ingredientes con ese nombre'})

        return jsonify([{
            'idProducto': prod.idProducto,
            'nombre': prod.nombre,
            'Tipo Producto': prod.tipo_producto,
            'Presentacion': prod.presentacion
        } for prod in productos])       


class IngredientesList(Resource):
    def get(self):
        ingredientes = Ingredientes.query.all()
        return jsonify([{
            'idIngrediente': ing.idIngrediente,
            'nombre': ing.nombre,
            'precio': ing.precio,
            'tipo_ingrediente': ing.tipo_ingrediente,
            'inventario': ing.inventario
        } for ing in ingredientes])

class IngredienteporID(Resource):
    def get(self, id):
        ingrediente = Ingredientes.query.get_or_404(id)
        return jsonify({
            'idIngrediente': ingrediente.idIngrediente,
            'nombre': ingrediente.nombre,
            'precio': ingrediente.precio,
            'tipo_ingrediente': ingrediente.tipo_ingrediente,
            'inventario': ingrediente.inventario
        })
        
        
class IngredienteporNombre(Resource):
    def get(self):
        nombre = request.args.get('nombre', None)
        if nombre is None:
            return jsonify({'error': 'Debe proporcionar un nombre de ingrediente'}), 400

        ingredientes = Ingredientes.query.filter(Ingredientes.nombre.like(f"%{nombre}%")).all()
        if not ingredientes:
            return jsonify({'message': 'No se encontraron ingredientes con ese nombre'})

        return jsonify([{
            'idIngrediente': ing.idIngrediente,
            'nombre': ing.nombre,
            'precio': ing.precio,
            'tipo_ingrediente': ing.tipo_ingrediente,
            'inventario': ing.inventario
        } for ing in ingredientes])


class AbastecerIngrediente(Resource):
    def get(self, id):
        try:
            ingrediente = Ingredientes.abastecer(id)
            return jsonify({
                'idIngrediente': ingrediente.idIngrediente,
                'nombre': ingrediente.nombre,
                'precio': ingrediente.precio,
                'tipo_ingrediente': ingrediente.tipo_ingrediente,
                'inventario': ingrediente.inventario,
                'message': 'Ingrediente abastecido exitosamente'
            })
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        

class IngredienteSano(Resource):
    def get(self, id):
        try:
            ingrediente = Ingredientes.es_sano(id)
            return jsonify({
                'Ingrediente Es Sano? :': ingrediente
            })
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        

class RenovarInventario(Resource):
    def get(self, id):
        try:
            ingrediente = Ingredientes.renovar_inventario(id)
            return jsonify({
                'Mensaje': ingrediente
            })
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        
class Vender(Resource):
    def get(self, id):
        producto = Productos.query.get_or_404(id)
        
        # Obtener todos los ingredientes
        ingredientes = Ingredientes.query.all()
        if len(ingredientes) < 3:
            return jsonify({'error': 'No hay suficientes ingredientes disponibles para hacer la venta'}), 400

        # Seleccionar 3 ingredientes aleatoriamente
        ingredientes_seleccionados = random.sample(ingredientes, 3)
        id_ingrediente_1 = ingredientes_seleccionados[0].idIngrediente
        id_ingrediente_2 = ingredientes_seleccionados[1].idIngrediente
        id_ingrediente_3 = ingredientes_seleccionados[2].idIngrediente

        
        precio_base = sum(ing.precio for ing in ingredientes_seleccionados)
        precio_total = precio_base
        precioPublico = producto.precio_publico

        if producto.tipo_producto == 'Malteada':
            precio_plastico = 500
            precio_total += precio_plastico
        else:
            precio_plastico = 0

        venta = Ventas(
            producto=producto.idProducto,
            ingrediente_1=id_ingrediente_1,
            ingrediente_2=id_ingrediente_2,
            ingrediente_3=id_ingrediente_3,
            precio_base=precio_base,
            precio_plastico=precio_plastico,
            precio_total=precio_total,
            precio_publico = precioPublico
            
        )
        db.session.add(venta)

        for ing in ingredientes_seleccionados:
            if ing.tipo_ingrediente == 'Base':
                ing.inventario -= 1
            elif ing.tipo_ingrediente == 'Complemento':
                ing.inventario -= 0.2

        db.session.commit()

        return jsonify({
            'idVenta': venta.idVenta,
            'fecha_venta': venta.fecha_venta,
            'idProducto': venta.producto,
            'ingrediente_1': venta.ingrediente_1,
            'ingrediente_2': venta.ingrediente_2,
            'ingrediente_3': venta.ingrediente_3,
            'precio_base': venta.precio_base,
            'precio_plastico': venta.precio_plastico,
            'precio_total': venta.precio_total,
            'precio_publico': venta.precio_publico,
            'message': 'Venta realizada exitosamente'
        })
        
        
class CostoProducto(Resource):
    def get(self,id):
        
        if id is None:
            return jsonify({'error': 'Debe proporcionar el idProducto'}), 400
        
        ventas = Ventas.query.filter_by(producto=id).join(Productos, Ventas.producto==Productos.idProducto).all()
        
        if not ventas:
            return jsonify({'message': 'No se encontraron ventas para el producto especificado'})
        
        return jsonify([{
            'Nombre Producto': venta.productos.nombre,
            'Costo Ingredientes': venta.precio_base,
            'Costo Plastico': venta.precio_plastico,
            'Costo Produccion': venta.precio_total
        } for venta in ventas])



