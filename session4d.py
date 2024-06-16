# promocode = ZOMOATO
# Condition1 = amount >249
# Condition2 = 50 % discount upto 150

promocode = input ( "please enter te promocode : ")
amount = int(input("please enter the amount : "))


# CONDITIONAL CONSTRUCT
if promocode == "ZOMATO":
    print ("promocode is valid")
    
    if amount > 249:
        print("promocode applied..")
        discount = (0.50 * amount)
        if discount >= 150:
            discount = 150
            print("your discount is ", discount)
        print ("please pay ", (amount - discount))
    else:
        print("amount is low..")
        print("please Buy items worth", (249 - amount), "more..")
else:
    print("promocode is invalid")