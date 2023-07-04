def avg(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print("Avg = ", sum/len(number))

avg(5,6,7,8)

#  for dictionary 
def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"] )
    print(type(name))
name(mname = "David", lname = "Warner", fname = "Jhon")