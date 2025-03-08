# dict1 = {
#     1 : "zisha",
#     2 : "sia",
#     3 : "kia",
#     4 : "himani",
#     5 : "riya",
#     5 : "priya"
# }

# print("dict1 :" ,dict1)
# print(len(dict1))
# print(min(dict1))
# print(max(dict1))
# print(sum(dict1))

# dict1 = {
#     "a": "zisha",
#     "b": "sia",
#     "c": "kia",
#     "d": "himani",
#     "e": "riya",
#     "f": "priya"
# }


# print("dict1 :" ,dict1)
# print(len(dict1))
# print(min(dict1))
# print(max(dict1))
# # print(sum(dict1))

# subject = ["science" , "maths" , " english" , "ssc" , "english"]
# marks = {}.fromkeys(subject, 67)
# print(marks)

# keys  =  dict1.keys()
# print(keys)

covid_data = {
    "usa": [786167, 40333, 985],
    "india": [786167, 40333, 985],
    "brazil": [786167, 40333, 985],
    "italy": [786167, 40333, 985],
    "uk": [786167, 40333, 985],
}

covid_data_world = {
    "usa": {"active":786167, "serious":40333, "recovered":985},
    "india": {"active":226167, "serious":2344, "recovered":1985},
    "brazil": {"active":96167, "serious":1221, "recovered":850},
    "italy": {"active":18167, "serious":4433, "recovered":3185},
    "uk": {"active":61670, "serious":6722, "recovered":9098},
}

# Write the Logic to copmute below data
# 1: Total Active
# 2: Total Serious
# 3: Total Recovered

# 4: Min/Max Active/Serious/recovered on Country

# 5: To compute Average of all Active/Serious/Recovered in world

items = covid_data_world.items()
items = tuple(items)
active = list()
serious = list()
recovered = list()
data = list(items[0][1].values())
am = data[0]
sm = data[1]
rm = data[2]
amax = data[0]
smax = data[1]
rmax= data[2]
for idx in range(0 , len(items)):
    data =list(items[idx][1].values())
    if am > data[0]:
        am = data[0]
    if amax < data[0]:
        amax = data[0]

    if sm > data[1]:
        sm = data[1]
    if smax < data[1]:
        smax = data[1]

    if rm > data[2]:
        rm = data[2]
    if rmax < data[2]:
        rmax = data[2]

    active.append(data[0])
    serious.append(data[1])
    recovered.append(data[2])



print("total active :" ,sum(active))
print("average active :" ,sum(active)/len(active))
print("minimum active :" , am)
print("maximum active :" , amax)
print("=================================")
print("total serious :" ,sum(serious))
print("average serious :" ,sum(serious)/len(serious))
print("minimum serious :" , sm)
print("maximum serious :" , smax)
print("=================================")
print("total recovered :" ,sum(recovered))
print("average recovered :" ,sum(recovered)/len(recovered))
print("minimum recovered :", rm)
print("maximum recovered :", rmax)
print("=================================")

# ======optimal approach==========
#make a list using this ->
active_users = [data['active'] for data in covid_data_world.values()]
print(active_users)#--> return list of active users