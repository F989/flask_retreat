from utils.dal import DAL

from utils.image_handler import ImageHandler
from models.vacation_model import *
from models.client_error import *

class VacationLogic:
    def __init__(self):
        self.dal = DAL()
    

    
    def get_all_vacation_ordered_by_date(self):
        sql = """
        SELECT v.vacationId, v.v_description, v.StartDay, v.LastDay, v.price, v.image_name, c.country,
            COUNT(l.userId) AS like_count  -- Count the number of users who liked the vacation
        FROM vacations AS v
        JOIN countries AS c ON v.countryId = c.countryId
        LEFT JOIN likes AS l ON v.vacationId = l.vacationId
        GROUP BY v.vacationId, v.v_description, v.StartDay, v.LastDay, v.price, v.image_name, c.country
        ORDER BY v.StartDay ASC;
        """
        return self.dal.get_table(sql)



    # def get_all_vacation_ordered_by_date(self):
    #     sql = """
    #     SELECT v.vacationId, v.v_description, v.StartDay, v.LastDay, v.price, v.image_name, c.country
    #     FROM vacations AS v
    #     JOIN countries AS c ON v.countryId = c.countryId
    #     ORDER BY v.StartDay ASC;
    #     """
    #     return self.dal.get_table(sql)
       
    
    def get_one_vacation(self, vacationId):
        sql = """
        SELECT v.vacationId, v.v_description, v.StartDay, v.LastDay, v.price, v.image_name, c.country
        FROM vacations AS v
        JOIN countries AS c ON v.countryId = c.countryId
        WHERE v.vacationId = %s;
        """
        return self.dal.get_one_row(sql, (vacationId,))
      
    
    def add_new_vacation(self, vacation):
        image_name = ImageHandler.save_image(vacation.image)
        sql = "INSERT INTO vacations (v_description, StartDay, LastDay, price, image_name, countryId) VALUES (%s, %s, %s, %s, %s, %s)"
        row_id = self.dal.insert(sql, (vacation.v_description, vacation.StartDay, vacation.LastDay, vacation.price, image_name, vacation.countryId))
        return row_id 
    
    
    def update_vacation(self, vacation):
        old_image_name = self.get_old_image_name(vacation.vacationId) if vacation.vacationId else None
        image_name = ImageHandler.update_image(old_image_name, vacation.image)
        
        sql = "UPDATE vacations SET v_description = %s, StartDay = %s, LastDay = %s, price = %s, image_name = %s, countryId = %s WHERE vacationId = %s"
        params = (vacation.v_description, vacation.StartDay, vacation.LastDay, vacation.price, image_name, vacation.countryId, vacation.vacationId)
        row_count = self.dal.update(sql, params)
        return row_count

   
    
    def get_old_image_name(self, vacationId):
        sql = "SELECT image_name FROM vacations WHERE vacationId = %s"
        result = self.dal.get_one_row(sql, (vacationId,))
        return result["image_name"]
    
    def delete_vacation(self, vacationId):
        image_name = self.get_old_image_name(vacationId)
        ImageHandler.delete_image(image_name)
        
        sql = "DELETE FROM vacations WHERE vacationId = %s"
        params = (vacationId,)
        row_count = self.dal.delete(sql, params)
        return row_count
    

    def vacationId_not_in_system(self, vacationId):
        sql = "SELECT vacationId FROM vacations WHERE vacationId = %s"
        params = (vacationId,)
        vacationId = self.dal.get_one_row(sql, params)
        return vacationId is None

    def countryId_does_not_exist(self, countryId):
        sql = "SELECT countryId FROM countries WHERE countryId = %s"
        params = (countryId,)
        countryId = self.dal.get_one_row(sql, params)
        return countryId is None
    
    def get_all_countries(self):
        sql = "SELECT * FROM countries"  
        return self.dal.get_table(sql)


    def close(self):
        self.dal.close()
  
    
  
    
    



    