from validate_email_address import validate_email

class CredentialModel:
    def __init__(self, Email, Password):
        
        self.Email = Email 
        self.Password = Password 


    def validate(self):
        if not self.Email:return "Email"
        if not self.Password:return "Password"
        if not validate_email(self.Email): return "not validate not correct"
        return None

