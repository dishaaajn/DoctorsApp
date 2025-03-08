import mysql.connector as db

class database :
    def __init__ (self):
        self.connection = db.connect (user="root" , password = "disha" ,host = "127.0.0.1" , database ="disha")
        print("connection created")
        self.cursor = self.connection.cursor()
        print("cursor created!!")

    #update , insert , delete 
    def write (self, sql):
        self.cursor.execute(sql)

        print("[database] database updated")
        self.connection.commit()
        print("changes in the transaction are committed!!")

    def read (self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

