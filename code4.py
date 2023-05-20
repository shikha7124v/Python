# Number data type - float and integer 
num1 = 5
num2 = 2
sub = num1 - num2 
add = num1 + num2
print("Num1 = " + str(num1) +" and num2 = "+ str(num2) + " having addition = "+ str(add) + " and subtraction  = "+ str(sub))

power = num1 ** num2
print(power)
print(type(power))

pow = float(power)   #type casting
print(type(pow))

floatnum1 = 7.87655
print(type(floatnum1))

print(round(floatnum1))   #complete round off to integen 
print(round(floatnum1, 2))  #round off up to 2 decimal places 

import math

print(math.factorial(5))

print(math.ceil(2.2)) #round up

print(math.floor(2.2)) #round down

print(math.log(10))

print(math.pi)
