# t1 = (34 , 56 , 76 ,87 , 35)
# # t1.append(27)
# # t1.append(88)
# # t1.append(67)
# # t1.append(78)
# print(t1)

# print (len(t1))
# print (sum(t1))
# print (min(t1))
# print (max(t1))
# print (sum(t1)/ len(t1))
# result = tuple(reversed(t1))
# print(result)
# def reversed( data):

#     hIdx = len(data) -1
#     newList=[]
#     for idx in range(0 , hIdx+1):
#         newList.append(data[idx+hIdx])
#         hIdx-=2

#     print(newList)


# data = [10 , 20 , 30 , 40 ,50 , 90 , 56 , 78 ,34 ,67 , 34]
# reversed(data)

data = [24, 47 , 39 , 46 , 31 , 56 , 76 , 89]

length = len(data)
for idx in range (0 , length//2):
    n = data[idx]
    data[idx] = data[(length-1)-idx]
    data[(length-1)-idx] = n

print(data)

