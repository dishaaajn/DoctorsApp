"""
create table patient(
    cid int primary key auto_increment,
    name varchar (256),
    id varchar (256),
    phone varchar (20),
    email varchar (256),
    gender varchar (10),
    emergency_contact varchar (30),
    dob varchar (30),
    admitted_on datetime
);"""
import datetime
class patient:

    def __init__(self ,pid , name="", phone="" , email="" , gender="" , emergency_contact="" , dob="" , admitted_on="") :
        self.pid = pid
        self.name =   name 
        self.phone  =phone 
        self.email  =email 
        self.gender  =gender 
        self.emergency_contact  =emergency_contact 
        self.dob  =dob 
        self.admitted_on  = datetime.datetime.now()

    def add_patient_details(self):
        self.name  =input("enter patient's name : ")
        self.phone  =input("enter patient's phone no. : ")
        self.email  =input("enter patient's email : ")
        self.gender  =input("enter patient's gender :")
        self.emergency_contact  =input("enter patient's emergency contact : ")
        self.dob  =input("enter patient's dob : ")

    def update_patient_details(self):
        name  =input("enter patient's name : ")
        if name != "":
            self.name = name
        
        phone  =input("enter patient's phone no. : ")
        if phone != "":
            self.phone = phone

        email  =input("enter patient's email : ")
        if email != "":
            self.email = email

        gender  =input("enter patient's gender :")
        if gender != "":
            self.gender= gender

        emergency_contact  =input("enter patient's emergency contact : ")
        if emergency_contact != "":
            self.emergency_contact=emergency_contact
            
        dob  =input("enter patient's dob : ")
        if dob != "":
            self.dob= dob

    def show(self):        
        print ("PATIENT'S NAME = {} | ".format(self.name))        
        print ("PATIENT'S PHONE = {} | PATIENT'S EMAIL = {}".format(self.phone , self.email))
        print ("PATIENT'S GENDER = {} | PATIENT'S EMERGENCY CONTACT = {}".format(self.gender , self.emergency_contact))
        print ("PATIENT'S DOB = {} | PATIENT'S ADMITTED ON = {}".format(self.dob , self.admitted_on))


