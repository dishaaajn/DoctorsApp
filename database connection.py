import mysql.connector as db
from customer import customer

connection = db.connect(user = "root",
                        password = "disha",
                        host = "127.0.0.1",
                        database = "disha"
                        )

print("connection created")
print(connection)


c1 = customer()
c1.add_customer_details()

SQL ="insert into customer values(null , '{}' , '{}' ,'{}' , '{}','{}')".format(c1.name ,c1.phone ,c1.email , c1.age , c1.gender)


"""insert into customer values(null ,'riya' , 'pranjal' , 23 , 'bcom' , 'a' , 'male' , 'dance)"""

cursor = connection.cursor()
cursor.execute(SQL)
connection.commit()
cursor = connection.cursor()
cursor.execute("insert into customer values({})")
rows = cursor.fetchall()
for row in rows:
    print (row)
print("sql comand executed..")