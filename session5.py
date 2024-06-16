"""
ZOMATO = 20% off
       : min value = 300

BINGO =  50% off
      : min value = 500
      : max discount = 100
"""
amount = float(input ("please enter the amount : \u20b9"))
promocode= input ("please enter the promocode :")

if promocode == "ZOMATO":
    print("promocode valid")
    print ("promocode is applied..")

    if amount >= 300:
        discount = 0.20 * amount
        print("your discount is: \u20b9", discount, " Please pay \u20b9", (amount-discount)+(0.18*amount)+100)
    else:
        print("amount is low, please buy items worth \u20b9",(300-amount), "more..")

elif promocode == "BINGO":
    print("promocode valid")
    if amount >= 500:
        discount = 0.50*amount
        if discount > 100:
            discount = 100
        print ("your discount is \u20b9",discount, "please pay \u20b9",(amount- discount)+(0.18*amount)+100 )
    else:
        print("amount is low..please buy items worth \u20b9", (500 - amount,"more.."))
else:
    print("promoxcode is invalid")
print(" \u1F60 ")