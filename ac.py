"""create table customer(
    cid int primary key auto_increment,
    name varchar (256),
    phone varchar (20),
    email varchar (256),
    gender varchar (10)
);"""
class customer:
    def __init__(self , cid ,name , phone , email , gender  ) :
        self.cid= cid
        self.name = name 
        self.phone = phone
        self.email = email
        self.gender = gender

    def add_customer_details(self):
        
        self.name = input("enter customer's name :") 
        self.phone = input("enter customer's phone no. :")
        self.email = input("enter customer's email :")
        self.gender = input("enter customer's gender :")
        

    def show(self):

        print("""
        {cid} | {name}
        {phone} | {email}
        {gender} | 
        """.format(self.cid , self.phone , self.email , self.gender ))




        
