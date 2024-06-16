promo_code = "GET200"
min_amount = 500

amount = float(input("enter your amount: "))
if amount > min_amount:
    print("you can apply the promocode :)")
    print ("please pay", (amount - 200))
else:
    print("you cannot apply the promocode :(")
    print("please add items worth ",(min_amount - amount),"more..")
