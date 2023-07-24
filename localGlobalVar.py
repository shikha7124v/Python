# Local and Global Variable 
x = 5
print(x)

# def hello():
#     x = 7
#     print(f"The local x is {x}") #local because it's inside the function
#     print("Hii")

# print(f"The global x is {x}")    #global because it's outside the function
# hello()
 
# print(f"The global x is {x}")    #global because it's outside the function

# if i want to change the global variable
def changeTheGlobalVar():
    global x
    x = 10
    print(f"original value of global variable will print as {x}")

changeTheGlobalVar()
print(f"The global variable x get changed from inside the function, so the value from outside the function as {x}")