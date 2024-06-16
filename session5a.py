names=["disha" ,"arsh" , "arshita" , "mannat" , "rakhi"]
instagram_usernames =["dishaajn" , "arshjindal" , "arshhita" , "manu76" , "the.starlight.tarots"]

username = input ("enter the username: ")
idx = 0

while idx < len(instagram_usernames):
    if username == instagram_usernames[idx]:
        print(names[idx])
        break
    else:
        idx+=1
print("username not found")


for idx in range(0,len(instagram_usernames)):

    if username == instagram_usernames[idx]:
        print(names[idx])
        break
    else:
        idx+=1
print("username not found")    
