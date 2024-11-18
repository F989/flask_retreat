from hashlib import sha512
from utils.app_config import AppConfig
class Cyber:
    @staticmethod
    def hash(plain_text):
        encoded_text = plain_text.encode("utf-8") + AppConfig.password_salt.encode("utf-8") 
        hashed_text = sha512(encoded_text).hexdigest()
        return hashed_text