from flask import render_template, make_response, request, redirect, url_for, flash
from flask_restful import Resource
from flask_login import login_required, login_user
from db import db, login_manager

from models.usuarios import Usuarios
from models.roles import Roles


  
    

class UsuarioController(Resource):

    def get(self):
        
            return make_response(render_template("login.html"))
        
    def post(self):    
            username = request.form['username']
            password = request.form['password']
            user = Usuarios.query.filter_by(username=username, password=password).first()
            if user:
                login_user(user)
                

                return redirect(url_for("productoscontroller"))
                
            return make_response(render_template("login.html"))
        


        

