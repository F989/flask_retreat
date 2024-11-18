from validate_email_address import validate_email
from models.role_model import * 



class UserModel:

    def __init__(self,userId,fname,lname,Email,Password,roleId):
        self.userId = userId
        self.fname = fname
        self.lname = lname
        self.Email = Email
        self.Password = Password
        self.roleId = roleId

    def __str__(self):
        return (f"userId: {self.userId},fname: {self.fname},lname: {self.lname},Email: {self.Email},Password: {self.Password},roleId: {self.roleId} ")

    @staticmethod
    def dictionary_to_user(dictionary):
        if dictionary is None:
            return None
        userId = dictionary.get("userId")  
        fname = dictionary.get('fname')
        lname = dictionary.get('lname')
        Email = dictionary.get('Email')
        Password = dictionary.get('Password')
        roleId = dictionary.get('roleId')
        user = UserModel(userId, fname, lname, Email, Password, roleId)
        return user

 
    
    @staticmethod
    def dictionaries_to_users(list_of_dictionary):
        users = []
        for item in list_of_dictionary:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
        return users
 
 

    def validate_insert(self):
        if not self.fname:return "missing fname"
        if not self.lname:return "missing lname"
        if not self.Email:return "missing Email"
        if not self.Password:return "missing password"
        if not self.roleId:return "missing roleId"
        if len(self.fname) < 2 or len(self.fname) > 20:return "first name must be 0-20"
        if len(self.lname) < 2 or len(self.lname) > 20:return "last name  must be 0-20"
        if len(self.Password) < 5 or len(self.Password) >225:return "password must be 5-225"
        if not validate_email(self.Email): return "email not valid"
        if self.roleId != RoleModel.Admin.value and self.roleId!=RoleModel.User.value : "not valid role"
        return None



    