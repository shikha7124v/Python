# Match case statement 
'''
import os 
print("Hello world from...")
os.system("Python --version")
'''

def switch(x):
    if x == 0:
        print("It's Zero: ")
    elif x == 1:
        print("It's One: ")
    else:
        print("Error!!!")

x = int(input("Print either 0 or 1, x = "))
switch(x)

'''
match x:
    case 0:
        print("you have printed zero")
    case 1: 
        print("You have printed one")
    case _: 
        print("Error!!!")
'''
