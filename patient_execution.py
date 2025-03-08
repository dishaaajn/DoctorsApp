"""
create table patient(
    pid int primary key auto_increment,
    name varchar (256),
    phone varchar (20),
    email varchar (256),
    gender varchar (10),
    emergency_contact varchar (30),
    dob varchar (30),
    admitted_on datetime
);
"""

from patient import patient 
from databaseall import database
from tabulate import tabulate


while True:
    print("--------WELCOME TO PATIENT MANAGEMENT APP--------")
    print("Choice 1 : Add a new patient")
    print("Choice 2 : Update an existing patient's details")
    print("Choice 3 : Discharge an existing patient by PID")
    print("Choice 4 : Discharge an existing patient by phone")
    print("Choice 5 : View a patient by PID")
    print("Choice 6 : View a Patient by phone")
    print("Choice 7 : View all patients")
    print("Choice 0 : Quit ")
    Db = database()
    choice = int (input("enter your choice : "))
    if choice == 1:

        p1 = patient()
        p1.add_patient_details()
        p1.show()
        sql = "insert into patient values(null , '{name}' , '{phone}', '{email}' , '{gender}' , '{emergency_contact}' , '{dob}' , '{admitted_on}')".format_map(vars(p1))
        Db.write(sql)

    elif choice == 2:

        pid = int(input("enter the pid of the patient to be updated = "))
        sql = "select * from patient where pid = {}".format(pid)
        rows = Db.read(sql)
        print(rows)
        P1 = patient(  pid = rows[0][0] ,name= rows[0][1], phone = rows[0][2] , email = rows[0][3] , gender = rows[0][4] ,emergency_contact= rows[0][5] , dob=rows[0][6])

        P1.update_patient_details()
        P1.show()
        sql = "update patient set name = '{name}' , phone = '{phone}' , email = '{email}' , gender= = '{gender}' , emergency contact = '{emergency_contact}' , dob = '{dob}' , admitted on = '{admitted_on}' where pid = {pid}".format_map(vars(P1) ),pid
        Db.write(sql)

    elif choice == 3:

        CID = int(input("enter the cid of the patient to be discharged = "))
        sql = "delete from patient where cid = {}".format(CID)
        Db.write(sql)

    elif choice == 4:

        phone = int(input("enter the phone no. of the patient to be discharged = "))
        sql = "delete from patient where phone = '{}'".format(phone)
        Db.write(sql)

    elif choice == 5:

        cid = int(input("enter the cid of the patient to be discharged = "))
        sql = "select * from patient where cid = {}".format(pid)
        rows = Db.read(sql)
        columns = [ "cid" , "name"  , "phone" , "email" , "gender", "emergency_contact" ,"dob"   , "admitted_on"]
        # for row in rows :
        #     print(row)
        print (tabulate(  rows, headers = columns, tablefmt='grid'))

        

    elif choice == 6:

        phone = int(input("enter the phone no. of the patient to be discharged = "))
        sql = "select * from patient where phone = '{}'".format(phone)
        Db.read(sql)

        

    elif choice == 7:

        sql = "select * from patient"
        rows =Db.read(sql)
        columns = [ "pid" , "name"    , "phone" , "email" , "gender", "emergency_contact" ,"dob"   , "admitted_on"]
        # for row in rows :
        #     print(row)
        print (tabulate(  rows, headers = columns, tablefmt='grid'))


    elif choice == 0:

        break

    else :

        print("Incorrect Choice")
    
    