import mysql.connector as db

class database:
    def __init__(self):
        self.connection = db.connect(user = "root",
                                     password = "disha",
                                     host = "127.0.0.1",
                                     database = "disha")
        print("[database] connection created")
        
        self.cursor = self.connection.cursor()
        print("[database] cursor created")

#insert , update , delete
    def write(self , sql):
        self.cursor.execute(sql)
        self.connection.commit()

# select
    def read(self):
        pass