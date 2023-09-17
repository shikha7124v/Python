# If your function can take in any number of arguments then add a* in front of the parameter name.

def myFunc(*arguments):
    for a in arguments:
        print(a)
a = 2
b = 3
c = 4
myFunc(a)
myFunc(a,b)
myFunc(a,b,c)