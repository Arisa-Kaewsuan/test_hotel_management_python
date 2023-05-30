import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class connectDB():
    # Class variables
    db_config = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )
    
    def __init__(self,sql):
        self.sql = sql

    def connect_db(self):
        mydb = self.db_config
        return mydb
        
    def create_db(self,floor,room):  
        floor = floor
        room = room
        
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        
        sql = self.sql
        # print("input sql success : " + sql)
        
        try:
            mycursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return
            # print("Something went wrong: {}".format(err))
            
    def insert_db(self,val):
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        
        sql = self.sql
        val = val
        try:
            mycursor.execute(sql,val)
            mydb.commit()
        except mysql.connector.IntegrityError as err:
            return
            # print("Error: {}".format(err))
            
    def update_db(self, val):
        mydb = self.connect_db()
        mycursor = mydb.cursor()

        sql = self.sql
        val = val
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.ProgrammingError as err:
            return
            
    def select_db(self, val):
        mydb = self.connect_db()
        mycursor = mydb.cursor()

        sql = self.sql
        val = val

        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        
        # print(result)
        return result
   


# use this class : connectDB -- create_db
# sql = "CREATE TABLE Hotel (name VARCHAR(255), address VARCHAR(255))"
# obj = connectDB(sql)
# obj.connect_db()
# obj.create_db()


# use this class : connectDB -- insert_db
# sql = "INSERT INTO Hotel (room_number) VALUES (%s)"
# room = [102]
# obj = connectDB(sql)
# obj.insert_db(room)


# use this class : connectDB -- select_db
# sql = "SELECT name_guest FROM Hotel WHERE room_number = %s"
# val = [203]
# obj = connectDB(sql)
# obj.select_db(val)
