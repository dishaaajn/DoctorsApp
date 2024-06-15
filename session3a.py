cart=[]
amountlist=[]
amount = 0
print("WELCOME TO THE FOODIES")
print("____________________")
menu={
    "noodles" : 100,
    "burger" : 50,
    "manchurian" : 70,
    "pizza" : 65,
    "momos" : 55
}

print(menu)
print()

while True:
    item = input("enter your item here and press 0 to quit :  ")

    if item == "0":
        break

    quantity = int(input("enter the quantity :"))


    cart.append(item)
    amountlist.append(menu[item]*quantity )
    amount += menu[item]*quantity

print("cart is :")
print(cart)
print("no. of items :", len(cart))
print("prices are :" ,amountlist)
print("amount =" , amount , sum(amountlist))
