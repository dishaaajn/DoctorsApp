# #                               _
# #  1. indexing                   |
# #  2. negative indexing          |
# #  3. slicing                    |
# #  4. concatanation               >-on sets
# #  5. multiplicity               |
# #  6. membership testing        _| 


# dict1 = { "num1" : 1 ,"num2": 2 ,"num3": 4 ,"num4" : 7}
# print(type(dict1))

# #indexing
# # print(dict1[2])
# #no indexing in sets and dict

# #negative indexing
# # print(dict1[-1])
# # negative indexing is also not allowed in sets and dict

# #slicing
# # print(dict1[0:])
# #slicing too not allowed in sets and dict

# #concatanation
# # dict2 = {"num5" : 0,"num6": 6 ,"num7" : 9 ,"num7" : 5}
# # dict3 = dict1 + dict2
# # print(dict3)
# #no concatanation in sets and sictionary object is allowed

# #multiplicity
# # dict2 = dict1*5
# # print(dict2)
# #not allowed in sets as well as dict objects

# #membership testing
# print(4 in dict1)
# print("num1" in dict1)
# #sets and dict object support mem,bership testing but i dict only key names are checked

t1 = (5 , 8 ,0 ,4)
print(t1[0])
t1.pop()
print(t1)