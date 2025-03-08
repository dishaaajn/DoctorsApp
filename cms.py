# CUSTOMER MANAGEMENT SYSTEM
from customer import customer

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO CUSTOMER MANAGEMENMT SYSTEM")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while(True):
    print("RULES TO FOLLOW:")
    print("Choice 1 = Add Cutomers")
    print("Choice 2 = View Cutomers")
    print("Choice 0 = Delete Cutomers")
    choice = int(input("enter your choice :"))

    if choice == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("THANKYOU FOR USING CUSTOMER MANAGEMENT SYSTEM")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break
    if choice ==1 :
        file = open("customer.csv" , "a")
        customer = customer()
        customer.add_customer_details()
        customer.show()
        data=customer.to_csv()
        file.write(data)
        file.close()
        print("data written")

    if choice ==2:
        file= open("customer.csv" , "r")
        lines =file.readlines()
        for line in lines:
            print(line)

        file.close()
        print("data written...")

