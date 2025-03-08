# attribute of a driver = name , age , licence_no , gender , email , phone , rating , vehicle
from vehicle import vehicle

class driver:

    def __init__(self ,  name = " " , age = " " , licence_no = " " , gender = " " , email = " " , phone = "" , rating = 2.5 , vehicle = vehicle("default vehicle")):
        self.name = name
        self.age = age
        self.licence_no = licence_no
        self.gender = gender 
        self.email = email
        self.phone = phone
        self.rating = rating
        self.vehicle = vehicle

    def add_driver_details(self):
        print(">> ADD DRIVER DETAILS")
        self.name = input("enter name :")
        self.age =input("enter age :")
        self.licence_no=input("enter licence no. :")
        self.gender=input("enter gender :")
        self.email = input("enter email :")
        self.phone =input("enter phone :")
        self.rating = input("enter rating :")
        self.vehicle = vehicle()
        self.vehicle.add_vehicle_details()

    def show(self):
        print("------------------DRIVER-----------------")
        print("NAME : {} | AGE : {}".format(self.name,self.age))
        print("LICENCE NO. : {} | GENDER : {}".format(self.licence_no,self.gender))
        print("EMAIL : {} | PHONE : {} ".format(self.email ,self.phone))
        print("RATING : {}".format(self.rating))
        print("------------------------------------------")

        self.vehicle.show()

    def to_csv (self):
        print("Driver:")
        data = "{} , {} , {} , {} , {} , {} , {}".format(self.name,self.age,self.licence_no,self.gender,self.email ,self.phone,self.rating )
        return data
    
# d1 = driver()
# d1.add_driver_details()
# d1.show()