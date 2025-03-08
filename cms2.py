from customer import customer
from database import database 

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO CUSTOMER MANAGEMENMT SYSTEM")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while(True):
        print("RULES TO FOLLOW:")
        print("Choice 1 = Add new Cutomers")
        print("Choice 2 = Update Existing Cutomers")
        print("Choice 3 = Delete Existing Cutomers")
        print("Choice 4 = View All Cutomers by phone")
        print("Choice 5 = View All Cutomers by CID")
        print("Choice 6 = View All Cutomers")
        print("Choice 0 = To Quit")

        choice = int(input("enter your choice :"))
        if choice == 1:
            c1 = customer()
            c1.add_customer_details()
            db = database()
            sql = "insert into customer values(null , '{name}' ,'{phone}' , '{email}' , '{age}' , '{gender}' , null)".format_map(vars(c1))
            db.write(sql)
            print("database updated")


        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 0:
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()