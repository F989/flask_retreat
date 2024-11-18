from logic.like_logic import LikeLogic
from flask import request
from models.like_model import *
from models.user_model import *

class LikeFacade:
    def __init__(self):
        self.logic = LikeLogic()


   
    def add_user_like(self, userId, vacationId):
        try:
            
            success = self.logic.add_user_like(userId, vacationId)
            if success:
                
                like_count = self.logic.get_like_count(vacationId)
                return like_count  
            return None
        except Exception as e:
            print(f"Error adding user like: {e}")
            return None

    def remove_user_like(self, userId, vacationId):
        try:
            
            success = self.logic.remove_user_like(userId, vacationId)
            if success:
                
                like_count = self.logic.get_like_count(vacationId)
                return like_count 
            return None
        except Exception as e:
            print(f"Error adding user like: {e}")
            return None
     
        
    

    
        


   
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.logic.close()





    
 

                
        
    