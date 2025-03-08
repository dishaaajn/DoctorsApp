def add(*args):
    sum=0
    for num in args:
        sum=sum+num
    return sum

print(add(4 ,5 ,7 , 4 , 10))

print("===================================")
def register(**kwargs):
    print(type(kwargs))    
    return(kwargs)


print(register(name="disha" , age=6 ,rollno=61 ) )