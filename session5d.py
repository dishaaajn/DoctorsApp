# What is a Function/Method/Procedure
# A function is a piece of code, which we use again and again
# It can have input, which is processed and you get an output

# f(x) = y
# where y is: x*x + 1
# x: 1 => 2
# x: 3 => 10
def f(x):
    y=x*x +1
    print("y -",y)

f(1)
f(4)
f(8)

def whole_square(x):
    return x**2

print(whole_square(7))
print(whole_square(12))
print(whole_square(13))