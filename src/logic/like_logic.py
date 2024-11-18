from utils.dal import *
from models.like_model import *
from models.user_model import *
from models.vacation_model import *

class LikeLogic:
    def __init__(self):
        self.dal = DAL()
    
    def add_user_like(self, userId, vacationId):
        insert_sql = "INSERT INTO likes (userId, vacationId) VALUES(%s, %s)"
        try:
            self.dal.insert(insert_sql, (userId, vacationId))
            return True
        except Exception as e:
            print(f"Error adding user like: {e}")
            return False
        
    def remove_user_like(self, userId, vacationId):
        delete_sql = "DELETE FROM likes WHERE userId = %s AND vacationId = %s"
        try:
            affected_rows = self.dal.delete(delete_sql, (userId, vacationId))
            return affected_rows > 0  
        except Exception as e:
            print(f"Error removing user like: {e}")
            return False    

    def get_like_count(self, vacationId):
        count_sql = "SELECT COUNT(*) AS like_count FROM likes WHERE vacationId = %s"
        result = self.dal.get_one_row(count_sql, (vacationId,))
        return result['like_count'] if result else 0
    

    
    
    

    def close(self):
        self.dal.close()

    
    
    
        
    

