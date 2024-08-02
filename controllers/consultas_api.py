from flask import Flask, jsonify, render_template, request, make_response
from flask_restful import Resource
from flask_login import login_required, current_user
from models.productos import Productos
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.ventas import Ventas
from models.sabores import Sabores
from db import db
import random
from auth import role_required


class ProductosList(Resource):
     
    def get(self):
        productos = Productos.query.all()
        return jsonify([{
            'idProducto': prod.idproducto,
            'nombre': prod.nombre,
            'Tipo Producto': prod.tipo_producto,
            'Presentacion': prod.presentacion
        } for prod in productos])
        

        
class ProductoporID(Resource):
    def get(self, id):
        producto = Productos.query.get_or_404(id)
        return jsonify({
            'idProducto': producto.idproducto,
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
            'idProducto': prod.idproducto,
            'nombre': prod.nombre,
            'Tipo Producto': prod.tipo_producto,
            'Presentacion': prod.presentacion
        } for prod in productos])       


class CaloriasporProducto(Resource):
    @role_required([1,2,3])
    def get(self,id):
        ventas = Ventas.query.filter_by(producto=id).all()

        if not ventas:
            return jsonify({'error': 'No se encontraron ventas para el producto especificado.'}), 404
        
        data = []
        for venta in ventas:
            calorias = venta.ContarCalorias()
            venta_data = {
                'producto': venta.productos.nombre,
                'calorias': calorias
            }
            if venta.ingrediente1.sabores.nombre == "Sin Sabor":
                venta_data['ingrediente_1'] = f"{venta.ingrediente1.nombre}"
            else:
                venta_data['ingrediente_1'] = f"{venta.ingrediente1.nombre} {venta.ingrediente1.sabores.nombre}"
            if venta.ingrediente2.sabores.nombre == "Sin Sabor":
                venta_data['ingrediente_2'] = f"{venta.ingrediente2.nombre}"
            else:
                venta_data['ingrediente_2'] = f"{venta.ingrediente2.nombre} {venta.ingrediente2.sabores.nombre}"
            if venta.ingrediente3.sabores.nombre == "Sin Sabor":
                venta_data['ingrediente_3'] = f"{venta.ingrediente3.nombre}"
            else:
                venta_data['ingrediente_3'] = f"{venta.ingrediente3.nombre} {venta.ingrediente3.sabores.nombre}"
                
            data.append(venta_data)
            
        return jsonify(data)


class Rentabilidad(Resource):
    @role_required([1]) 
    def get(self,id):
        
        if id is None:
            return jsonify({'error': 'Debe proporcionar el idProducto'}), 400
        
        ventas = Ventas.query.filter_by(producto=id).all()
        
        if not ventas:
            return jsonify({'message': 'No se encontraron ventas para el producto especificado'})
        
        return jsonify([{
            'Nombre Producto': venta.productos.nombre,
            'Id Venta': venta.idventa,
            'Rentabilidad': venta.precio_publico - venta.precio_total
        } for venta in ventas])
 
        
class CostoProducto(Resource):
    @role_required([1]) 
    def get(self,id):
        
        if id is None:
            return jsonify({'error': 'Debe proporcionar el idProducto'}), 400
        
        ventas = Ventas.query.filter_by(producto=id).all()
        
        if not ventas:
            return jsonify({'message': 'No se encontraron ventas para el producto especificado'})
        
        return jsonify([{
            'Nombre Producto': venta.productos.nombre,
            'Costo Ingredientes': venta.precio_base,
            'Costo Plastico': venta.precio_plastico,
            'Costo Produccion': venta.precio_total
        } for venta in ventas])


class Vender(Resource):
    @role_required([1,2,3])
    def get(self, id):
        producto = Productos.query.get_or_404(id)
        
        # Obtener todos los ingredientes
        ingredientes = Ingredientes.query.all()
        if len(ingredientes) < 3:
            return jsonify({'error': 'No hay suficientes ingredientes disponibles para hacer la venta'}), 400

        # Seleccionar 3 ingredientes aleatoriamente
        ingredientes_seleccionados = random.sample(ingredientes, 3)
        id_ingrediente_1 = ingredientes_seleccionados[0].idingrediente
        id_ingrediente_2 = ingredientes_seleccionados[1].idingrediente
        id_ingrediente_3 = ingredientes_seleccionados[2].idingrediente

        
        precio_base = sum(ing.precio for ing in ingredientes_seleccionados)
        precio_total = precio_base
        precioPublico = producto.precio_publico

        if producto.tipo_producto == 'Malteada':
            precio_plastico = 500
            precio_total += precio_plastico
        else:
            precio_plastico = 0

        venta = Ventas(
            producto=producto.idproducto,
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
            'idVenta': venta.idventa,
            'fecha_venta': venta.fecha_venta,
            'idProducto': venta.producto,
            'ingrediente_1': venta.ingrediente_1,
            'ingrediente_2': venta.ingrediente_2,
            'ingrediente_3': venta.ingrediente_3,
            'costo_ingredientes': venta.precio_base,
            'costo_plastico': venta.precio_plastico,
            'costo_total': venta.precio_total,
            'precio_publico': venta.precio_publico,
            'message': 'Venta realizada exitosamente'
        })


class IngredientesList(Resource):
    
    @role_required([1,2]) 
    def get(self):
        ingredientes = Ingredientes.query.all()
        
        ingredientes_list = []
        for ing in ingredientes:
            if ing.sabores.nombre == 'Sin Sabor':
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            else:
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre + " " + ing.sabores.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            ingredientes_list.append(ingrediente_data)
        
        return jsonify(ingredientes_list)
            

class IngredienteporID(Resource):
    
    @role_required([1,2]) 
    def get(self, id):
        ingredientes = Ingredientes.query.filter_by(idingrediente=id)

        ingredientes_list = []
        for ing in ingredientes:
            if ing.sabores.nombre == 'Sin Sabor':
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            else:
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre + " " + ing.sabores.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            ingredientes_list.append(ingrediente_data)
        
        return jsonify(ingredientes_list)
        
        
class IngredienteporNombre(Resource):
    
    @role_required([1,2]) 
    def get(self):
        nombre = request.args.get('nombre', None)
        if nombre is None:
            return jsonify({'error': 'Debe proporcionar un nombre de ingrediente'}), 400

        ingredientes = Ingredientes.query.filter(Ingredientes.nombre.like(f"%{nombre}%")).all()
        if not ingredientes:
            return jsonify({'message': 'No se encontraron ingredientes con ese nombre'})

        ingredientes_list = []
        for ing in ingredientes:
            if ing.sabores.nombre == 'Sin Sabor':
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            else:
                ingrediente_data = {
                    'idIngrediente': ing.idingrediente,
                    'nombre': ing.nombre + " " + ing.sabores.nombre,
                    'precio': ing.precio,
                    'tipo_ingrediente': ing.tipo_ingrediente,
                    'inventario': ing.inventario
                }
            ingredientes_list.append(ingrediente_data)
        
        return jsonify(ingredientes_list)

   
    
class IngredienteSano(Resource):
    @role_required([1,2]) 
    def get(self, id):
        try:
            ingrediente = Ingredientes.es_sano(id)
            return jsonify({
                'Ingrediente Es Sano? :': ingrediente
            })
        except ValueError as e:
            return jsonify({'error': str(e)}), 400



class AbastecerIngrediente(Resource):
    @role_required([1,2]) 
    def get(self, id):
        try:
            ingrediente = Ingredientes.abastecer(id)
            
            ingredientes_list = []
            if ingrediente.sabores.nombre == 'Sin Sabor':
                    ingrediente_data = {
                        'idIngrediente': ingrediente.idingrediente,
                        'nombre': ingrediente.nombre,
                        'precio': ingrediente.precio,
                        'tipo_ingrediente': ingrediente.tipo_ingrediente,
                        'inventario': ingrediente.inventario,
                        'message': 'Ingrediente abastecido exitosamente'
                    }
            else:
                    ingrediente_data = {
                        'idIngrediente': ingrediente.idingrediente,
                        'nombre': ingrediente.nombre + " " + ingrediente.sabores.nombre,
                        'precio': ingrediente.precio,
                        'tipo_ingrediente': ingrediente.tipo_ingrediente,
                        'inventario': ingrediente.inventario,
                        'message': 'Ingrediente abastecido exitosamente'
                    }
            ingredientes_list.append(ingrediente_data)
            
            return jsonify(ingredientes_list)
            
            
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
     

class RenovarInventario(Resource):
    @role_required([1,2]) 
    def get(self, id):
        try:
            ingrediente = Ingredientes.renovar_inventario(id)
            return jsonify({
                'Mensaje': ingrediente
            })
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
          
        
        
class ConsultarApis(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return make_response(render_template("api_generico.html"))
        else:
            if current_user.rol_usuario == 1:
                return make_response(render_template("api_admin.html", username=current_user.username))
            elif current_user.rol_usuario == 2:
                return make_response(render_template("api_empleado.html", username=current_user.username))
            elif current_user.rol_usuario == 3:
                return make_response(render_template("api_cliente.html", username=current_user.username))
            else:
                return make_response(render_template("api_generico.html"))





