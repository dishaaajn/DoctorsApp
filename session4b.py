 # bitwise operators -> &,^,|
num1 = 10  # 1 0 1 0
num2 = 8   # 1 0 0 0
print("num1 in binary =" , bin(num1))
print("num2 in binary =" , bin(num2))

result1 = num1 & num2 # 1 0 0 0 -> 8
result2 = num1 | num2 # 1 0 1 0 ->10
result3 = num1 ^ num2 # 0 0 1 0 ->2

print("result 1 is:" , result1)
print("result 2 is:" , result2)
print("result 3 is:" , result3)

# Shift operators
num1 = 8
num2 = 3
 # 8 >> 3
result1 = num1>>num2 # 8>>3 = 8/2 raised to the power of 3 = 1
print (num1, ">>" , num2 , "=" ,result1)

 # 8 << 3
result2 = num1<<num2 # 8<<3 = 8*2 raised to the power of 3 = 64
print (num1, "<<" , num2 , "=" ,result2)

# retrieving the value
result3 = result1<<num2 # 1 << 3 = 1*2^3 = 8(original no.)
print(result1 ,"<<", num2, "=" , result3 )
result3 = result2>>num2 # 64 >> 3= 64 / 2^3= 8 (originl no.)
print(result2 , ">>", num2,"=", result3)

# how is shifting done
# 13 = 
# 0 0 0 0  1 1 0 1
# >>3
# _ _ 0 0  0 0 1 1 = 3
# 13
# 0 0 0 0  1 1 0 1
# <<3
# 0 0 1 1  0 1 _ _              
print(-13 >> 2)
# write 13 in binary = 0 0 0 0  1 1 0 1
# 2's complement =     1 1 1 1  0 0 1 0
# add 1 =                            + 1
#                      1 1 1 1  0 0 1 1
# perform shifting =   _ _ 1 1  1 1 0 0
#                      1 1 1 1  1 1 0 0
#2's complement =      0 0 0 0  0 0 1 1
# add 1       =                     + 1
#                      0 0 0 0  0 1 0 0 --> -52                 