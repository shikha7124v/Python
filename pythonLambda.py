# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
'''x = lambda a: a+10
print(x(5))'''

'''x = lambda a, b: a*b
print(x(5,6))'''

'''x = lambda a, b, c: a+b*c
print(x(2,3,4))'''

# better when we use them as an anonymous function inside another function 
def myFunc(n):
    return lambda a: a*n
x = myFunc(8)
print(x(11))