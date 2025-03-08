class customer:

    def __init__(self , name="" , phone="" , email ="", age =0, gender="" , address="" , created_on = "") :
        self.name= name        
        self.phone= phone
        self.email= email
        self.address= address
        self.gender= gender
        self.age= age 
        self.created_on= created_on 


    def add_customer_details(self) :
        print(">>ADD CUSTOMER DETAILS")
        self.name= input("Enter Customer Name :")        
        self.phone=input("Enter Customer phone :")        
        self.email=input("Enter Customer email :")        
        self.gender=input("Enter Customer gender :")        
        self.age=input("Enter Customer age :")        
        self.address=input("Enter Customer address :")
        
    def show(self):
        print(">------------------CUSTOMER-----------------:")
        print("NAME : {} | PHONE : {}".format(self.name,self.phone))
        print("EMAIL : {} |GENDER : {}".format(self.email,self.gender))
        print("AGE : {} |  ADDRESS : {}".format(self.age ,self.address  ))
        print("CREATED ON : {} ".format(self.created_on  ))
        print("------------------------------------------")


    def to_csv (self):
        data = "{} , {} , {} , {} , {} , {} \n".format(self.name,self.phone,self.email,self.gender,self.age ,self.address )
        return data

        
