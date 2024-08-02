from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_login import LoginManager, login_required, login_user,logout_user, current_user
from flask_restful import Api, Resource
from dotenv import load_dotenv # type: ignore
from db import db
import os
from functools import wraps

from controllers.consultas_controller import IngredientesController, ProductosController, VentasController, CaloriasController

from controllers.heladeria_controller import HeladeriaController, HeladosVender
 
from controllers.inicio_controller import UsuarioController

from controllers.consultas_api import ConsultarApis, ProductosList, ProductoporID, ProductoporNombre, IngredientesList, IngredienteporID, IngredienteporNombre ,AbastecerIngrediente,IngredienteSano, IngredienteSano, RenovarInventario, Vender, CostoProducto, Rentabilidad, CaloriasporProducto

from models.usuarios import Usuarios
from auth import *


load_dotenv()

secret_key = os.urandom(24)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}:{os.getenv("PORT_DB")}/{os.getenv("SCHEMA_DB")}'
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    user = Usuarios.query.get(user_id)
    if user:
        return user
    return None


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return make_response(render_template("login.html"))


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(render_template("login.html"))



api.add_resource(ProductosController, "/")
api.add_resource(HeladeriaController, "/vender")
api.add_resource(UsuarioController, "/login")
api.add_resource(HeladosVender, '/heladosvender')
api.add_resource(IngredientesController, "/ingredientes")
api.add_resource(CaloriasController, "/calorias")
api.add_resource(VentasController, "/ventas")
api.add_resource(ConsultarApis, "/api")
api.add_resource(ProductosList, '/api/productos')
api.add_resource(ProductoporID, '/api/productos/<int:id>')
api.add_resource(ProductoporNombre, '/api/productos/nombre')
api.add_resource(CaloriasporProducto, '/api/calorias/<int:id>')
api.add_resource(Rentabilidad, '/api/rentabilidad/<int:id>')
api.add_resource(CostoProducto, '/api/costos/<int:id>')
api.add_resource(Vender, '/api/vender/<int:id>')
api.add_resource(IngredientesList, '/api/ingredientes')
api.add_resource(IngredienteporID, '/api/ingredientes/<int:id>')
api.add_resource(IngredienteporNombre, '/api/ingredientes/nombre')
api.add_resource(IngredienteSano, '/api/ingredientes/es_sano/<int:id>')
api.add_resource(AbastecerIngrediente, '/api/ingredientes/abastecer/<int:id>')
api.add_resource(RenovarInventario, '/api/ingredientes/renovar/<int:id>')





if __name__ == '__main__':
    app.run(debug=True)
