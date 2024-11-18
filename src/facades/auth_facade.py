from validate_email_address import validate_email
from flask import request, session
from logic.auth_logic import AuthLogic
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import *
from models.credential_model import *
from utils.cyber import Cyber

class CredentialModel:
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

    def validate(self):
        if not self.Email:
            return "Email is missing"
        if not self.Password:
            return "Password is missing"
        if not validate_email(self.Email):
            return "Invalid email address"
        return None

class AuthFacade:
    def __init__(self):
        self.logic = AuthLogic()

    def register(self):
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        Email = request.form.get("Email")
        Password = request.form.get("Password")
        user = UserModel(None, fname, lname, Email, Password, RoleModel.User.value)
        error = user.validate_insert()
        if error:
            raise ValidationError("Register error: " + error, user)
        if self.logic.is_email_taken(Email):
            raise ValidationError("Email already exists", user)
        user.Password = Cyber.hash(user.Password)
        self.logic.add_user(user)

    def login(self):
        Email = request.form.get("Email")
        Password = request.form.get("Password")

        credentials = CredentialModel(Email, Cyber.hash(Password))
        
        error = credentials.validate()
        if error:
            raise ValidationError(error, credentials)
        user = self.logic.get_user(credentials)
        if not user:
            raise AuthError("Incorrect email or Password", user)
        del user["Password"]
        session["current_user"] = user

    def block_anonymous(self):
        user = session.get("current_user")
        print(f"Checking block_anonymous: {user}")
        if not user:
            raise AuthError("You are not logged in")

    def block_non_admin(self):
        user = session.get("current_user")
        print(f"Current user in block_non_admin: {user}")
        if not user:
            raise AuthError("You are not logged in")
        if user["roleId"] != RoleModel.Admin.value:
            raise AuthError("You are not allowed")
        
    def block_admin(self):
        user = session.get("current_user")
        print(f"Current user in block_admin: {user}")
        
        if not user:
            raise AuthError("You are not logged in")
        
        if user["roleId"] == RoleModel.Admin.value:  
            raise AuthError("Admins are not allowed to perform this action")
     
    def logout(self):
        session.clear()

    def close(self):
       self.logic.close()

   