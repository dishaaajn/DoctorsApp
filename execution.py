from customer import customer
from driver import driver
from vehicle import vehicle
from ride import ride
import mysql.connector as db


# print("adding customer")
# c1 = customer()
# c1.add_customer_details()

# print("adding driver")
# d1 = driver()
# d1.add_driver_details()

# print("adding ride")
# r1 = ride()
# r1.add_ride_details()
# r1.link_customer(c1)
# r1.link_driver(d1)
# print("ride booked")
# r1.show()

print("YOU CAN LOGIN AS:")
print("Choice 1 = Customer")
print("Choice 2 = Driver")
print()
choice = input("Who are you? :").lower()
if choice == "customer":
    c1 = customer()
    connection = db.connect (user = "root", password = "disha" , host = "127.0.0.1" , database = "disha")    
    confirm="change"
    while confirm == "change":
        print("Enter Your Details")
        c1.add_customer_details()
        c1.show()
        confirm = input("Check the details.Type OK to confirm and CHANGE to change :").lower()
        if confirm == "ok":
            cursor=connection.cursor()
            print("making a query")
            SQL = "insert into customer values(null , '{}' , '{}' ,'{}' , '{}' ,'{}' ,'{}')".format(c1.name , c1.phone , c1.email , c1.age ,c1.gender , c1.address)
            cursor.execute(SQL)
            connection.commit()
            print("database updated")
            data=c1.to_csv()
            file = open("customer.csv" , "a")
            file.write(data)
            file.close()
            print ("You are registered as a customer successfully!")
            r1 = ride()
            print("Enter your ride details :")
            r1.add_ride_details()

elif choice == "driver":
    d1 = driver()
    confirm = "change"
    while confirm == "change" :
        print("Enter your details :")
        d1.add_driver_details()
        d1.show()
        confirm=input("Check the details.Type OK to confirm and CHANGE to change :").lower()
        if confirm == "ok":
                data=d1.to_csv()
                file = open("driver.csv" , "a")
                file.write(data)
                file.close()
                r1 = ride()
                print ("You are registered as a driver successfully!")


else: 
    print("incorrect choice")

if choice == "customer":
    r1.link_customer(c1)
    r1.show()
    print()
    print(">>>>>>>>>>RIDE BOOKED<<<<<<<<<<<<<<")

if choice == "driver":
    r1.link_driver(d1)
    r1.show()
    print()
    print(">>>>>>>>>>RIDE BOOKED<<<<<<<<<<<<<<")
