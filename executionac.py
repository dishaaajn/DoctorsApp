from ac import customer 
from databaseall import database
from tabulate import tabulate
from ac2 import ac


while True:
    print("--------WELCOME TO CUSTOMER MANAGEMENT APP--------")
    print("Choice 1 : Add a new customer")
    print("Choice 2 : Update an existing customer's details")
    print("Choice 3 : Delete an existing customer by CID")
    print("Choice 4 : Delete an existing customer phone")
    print("Choice 5 : View a customer by CID")
    print("Choice 6 : Add AC for a customer")
    print("Choice 7 : View AC of a customer")
    print("Choice 8 : View AC of all customer")
    print("Choice 9 : View a customer by phone")
    print("Choice 10 : View all customers")
    print("Choice 0 : Quit ")
    Db = database()
    choice = int (input("enter your choice : "))
    if choice == 1:
        c1 = customer()
        c1.add_customer_details()
        c1.show()
        sql ="insert into customer values(null , {name} , {phone} , {email} , {gender} )".format_map(vars(c1))
        Db.write(sql)
        print ("cudtomer added !!")

    elif choice == 2:
        sql ="update customer set name = '{name}' , phone = '{phone}' , email = '{email}'  , gender = '{gender}' "

    if choice ==6:
        cid = int(input("enter the cid of the ac owner :"))
        a1 = ac()
        a1.add_ac_details()
        a1.show()
        sql = "insert into ac values('{aid}' , '{model}' , '{brand}' , '{next_service_on}' , '{serviced_on}'where cid = {cid})".format_map(vars(a1)),cid

        rows = Db.write(sql)
        columns = ("aid" , "cid" , "model" , "brand" , "next_service_on" , "serviced_on")
        print(tabulate(rows , headers = columns , tablefmt="grid"))