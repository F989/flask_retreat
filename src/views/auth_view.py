from flask import Blueprint, render_template, send_file, url_for, redirect, request
from facades.auth_facade import AuthFacade
from models.client_error import * 
from models.credential_model import * 
from models.role_model import RoleModel

auth_blueprint=Blueprint("auth_view", __name__)

facade = AuthFacade() 

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET" : return render_template("register.html",active="register", user={})
        pass
        facade.register() 
        return redirect(url_for("vacations_view.list"))
    except ValidationError as err:
        return render_template("register.html", error = err.message)
    

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET": return render_template("login.html",credentials={},active="login" )
        facade.login() 
        return redirect(url_for("vacations_view.list"))
    except(ValidationError, AuthError) as err:
        return render_template("login.html", error = err.message, credentials = err.model)
 
@auth_blueprint.route("/logout")
def logout():
    facade.logout() 
    return redirect(url_for("vacations_view.list"))

