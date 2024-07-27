from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user
from flask_restful import Api # type: ignore
from dotenv import load_dotenv # type: ignore
from db import db, login_manager
import os

from controllers.consultas_controller import IngredientesController
from controllers.consultas_controller import ProductosController
from controllers.consultas_controller import VentasController
from controllers.heladeria_controller import HeladeriaController
from controllers.heladeria_controller import HeladosVender
from controllers.inicio_controller import UsuarioController
from controllers.consultas_api import ProductosList
from controllers.consultas_api import ProductoporID
from controllers.consultas_api import ProductoporNombre
from controllers.consultas_api import IngredientesList
from controllers.consultas_api import IngredienteporID
from controllers.consultas_api import IngredienteporNombre
from controllers.consultas_api import AbastecerIngrediente
from controllers.consultas_api import RenovarInventario
from controllers.consultas_api import IngredienteSano
from models.usuarios import Usuarios


load_dotenv()

secret_key = os.urandom(24)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
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






api.add_resource(HeladeriaController, "/")
api.add_resource(UsuarioController, "/login")
api.add_resource(HeladosVender, '/heladosvender')
api.add_resource(IngredientesController, "/ingredientes")
api.add_resource(ProductosController, "/productos")
api.add_resource(VentasController, "/ventas")
api.add_resource(ProductosList, '/api/productos')
api.add_resource(ProductoporID, '/api/productos/<int:id>')
api.add_resource(IngredientesList, '/api/ingredientes')
api.add_resource(IngredienteporID, '/api/ingredientes/<int:id>')
api.add_resource(IngredienteporNombre, '/api/ingredientes/nombre')
api.add_resource(AbastecerIngrediente, '/api/ingredientes/abastecer/<int:id>')
api.add_resource(ProductoporNombre, '/api/productos/nombre')
api.add_resource(IngredienteSano, '/api/ingredientes/es_sano/<int:id>')
api.add_resource(RenovarInventario, '/api/ingredientes/renovar/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
