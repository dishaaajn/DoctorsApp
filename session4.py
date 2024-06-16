cab_fare = 500
e_wallet = 300
print("can i book a cab ? ", (cab_fare<e_wallet))

email = input("enter your email :")
password =input("enter password :")
result = (email == "jaindisha931@gmail") and (password == "disha123")
print("is login successful?", result)

otp = 1804
user_otp = int(input("enter the otp recieved :"))
print("is otp is correct", otp == user_otp)

# membership testing
a = 10
bn= 10
print ( a == b, a is b)