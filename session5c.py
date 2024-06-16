product_series=[1200, 3400 ,5678 ,8645 ,3456 ,7563]
salaries=[35000 , 45000, 76500 , 34099 ,76568]
team_points=[12 , 5 ,3 ,17 ,8,56]

max=product_series[0]
for idx in range(1,len(product_series)):
    if product_series[idx] > max:
        max = product_series[idx]


print("max =",max)

max=salaries[0]
for idx in range(1,len(salaries)):
    if salaries[idx] > max:
        max = salaries[idx]


print("max =" ,max)

max=team_points[0]
for idx in range(1,len(team_points)):
    if team_points[idx] > max:
        max = team_points[idx]

        
print("max =",max)