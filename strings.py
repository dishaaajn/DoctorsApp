# email = input("enter your email")
# if "@" in email and "." in email:
#     print ("email is well formed :" , email )

# else :
#     print ("email is not correctly formed")

# contacts = ["john" , "disha" , "sia" , "priya" , "rajni" , "kajal" , "pranjal" , "ishant" , "surbhi"]
# search = input("enter your search keyword :")
# for contact in contacts :
#     if search in contact:
#         print (contact) 

def stripper (s , value=" "):
    forward_space= ""
    for char in s:
        if char==value:
            forward_space+=char
        if char!=value:
            break
    
    backward_space=""
    new = '' .join(reversed(s))
    for char in new:
        if char==value:
            backward_space+=char
        if char!=value:
            break
        
    result= new.removeprefix(backward_space)
    result = "".join(reversed(result))
    result = result.removeprefix(forward_space)

    return result



 
# quote = "disha jain"
# quote.upper()
# print(quote)
# print(id(quote))
# # print(str)
# # print(id(str))
# print(quote.upper())
# # print(id(quote.upper()))

# quote.lower()
# print(quote)
# print(id(quote))
# print(quote.title())
s1 = stripper("000000sheetal jha000000" , "0")
print(s1)
quote= "search the candle rather the  than cursing the darkness "
print(id(quote))
# print(quote.replace("the" , "disha")) 
print(quote.title())
print(id(quote))
idx1 = quote.rfind("the")
print(quote[idx1 : idx1+4])

# str = quote.lower()
# print(str)
# print(id(str))
# print(quote.lower())
# print(id(quote.lower()))
