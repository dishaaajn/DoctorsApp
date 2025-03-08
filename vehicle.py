# attributes for vehicle class = registration_no. , brand , model , color 

class vehicle:

    def __init__ (self, reg_number="NA", brand="NA", model="NA", color="white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        print(">> ADD VEHICLE DETAILS")
        self.reg_number = input("Enter Vehcile Registration Number: ")
        self.brand = input("Enter Vehcile Brand: ")
        self.model = input("Enter Vehcile Model: ")
        self.color = input("Enter Vehcile Color: ")
        if self.color=="":
            self.color="white" 

    def show(self):
        print("------------------VEHCILE-----------------")
        print("Number: {} | Brand: {}".format(self.reg_number, self.brand))
        print("Model: {} | Color: {}".format(self.model, self.color))
        print("------------------------------------------")

"""vh = vehicle()
vh.add_vehicle_details()
vh.show()"""