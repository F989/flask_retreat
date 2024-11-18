from utils.dal import DAL 
class AuthLogic:

    def __init__(self) -> None:
        self.dal = DAL() 

    def add_user(self, user):
        sql = "INSERT INTO users(fname, lname, Email, Password, roleId) VALUES(%s, %s, %s,%s, %s)"
        self.dal.insert(sql , (user.fname, user.lname, user.Email, user.Password, user.roleId))


    def is_email_taken(self, Email):
        sql  = "select EXISTS(select *from users where Email = %s) as is_taken"
        result = self.dal.get_one_row(sql, (Email,))
        return result["is_taken"] == 1 
    
    def get_user(self, credentials): 
        sql = "SELECT * FROM users where Email =%s and Password = %s"
        user = self.dal.get_one_row(sql, (credentials.Email, credentials.Password))
        return user 

    def close(self):
        self.dal.close(); 