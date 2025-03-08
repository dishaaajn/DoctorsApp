"""Ride: customer [1 to 1], date, time, from_location, to_location, distance, fare, driver [1 to 1]
    1 Ride has 1 Customer
    1 Ride has 1 Driver """
from customer import customer
from driver import driver
class ride :

    def __init__ (self , customer = None ,  date = "", time = "", from_location = "", to_location = "", distance = 0, fare = 0, driver = None):
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.distance = distance
        self.fare = fare
        self.customer = customer
        self.driver = driver
    def check_customer_and_driver_sync(self):
        if not self.customer:
            self.customer = customer("default customer")

        else:
            self.driver = driver("default driver")

    def link_customer(self , customer):
        self.customer = customer
        self.check_customer_and_driver_sync()

    def link_driver(self , driver):
        self.driver = driver
        self.check_customer_and_driver_sync()
        
    def add_ride_details(self):
        print(">>ADD RIDE DETAILS") 
        self.from_location=input("Enter from location :")        
        self.to_location=input("Enter to location :")        

    def show(self):

        print("------------------RIDE-----------------")
        print("DATE : {} | TIME : {}".format(self.date,self.time))
        print("FROM LOCATION : {} |TO LOCATION : {}".format(self.from_location,self.to_location))
        print("DISTANCE : {} |  FARE | ".format(self.distance ,self.fare  ))
        print("------------------------------------------")
        
        self.customer.show()
        self.driver.show()
        


