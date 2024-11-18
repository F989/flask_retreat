import mysql.connector
from utils.app_config import AppConfig
class DAL:

    
    def __init__(self):
            try:
            
             self.connection = mysql.connector.connect(host=AppConfig.mysql_host, user=AppConfig.mysql_user, password=AppConfig.mysql_password, database=AppConfig.mysql_database)

            except mysql.connector.Error as e:
                print("MySQL Connector Error:", e)
            
    
    def get_table(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table 
    
    def get_one_row(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            row = cursor.fetchone()
            return row 
    
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() 
            num_row_added = cursor.rowcount
            last_row_id = cursor.lastrowid
            if last_row_id == 0 :    #likes table has no likeId so it returns zero 
                return num_row_added #'number of rows added' value in likes table 
            else:
                return last_row_id 
                        
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() 
            row_count = cursor.rowcount
            return row_count
        
   
    

    def close(self):
        self.connection.close() 
