from flask import Flask, jsonify, render_template, request
from flask_restful import Resource
from models.productos import Productos
from models.ingredientes import Ingredientes
from models.productos import Productos


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


