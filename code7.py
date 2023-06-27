def switch(x):
    if x == 10:
        print("October")
    elif x == 11:
        print("November")
    elif x == 12:
        print("December")
    elif x == 1:
        print("January")
    elif x == 2:
        print("Feb")
    elif x== 3:
        print("March")
    elif x == 4:
        print("April")
    elif x == 5:
        print("May")
    elif x == 6:
        print("June")
    elif x == 7:
        print("July")
    elif x == 8:
        print("August")
    elif x == 9:
        print("September")
    else:
        print("Error!!!! Please enter a valid birth month. ")

x = int(input("Enter your birthday month in integer: "))
switch(x)


# match x:
#     case 1: print("Jan")
#     case 2: print("Feb")
#     case 3: print("Mar")
#     case 4: print("Apr")
#     case 5: print("May")
#     case 6: print("June")
#     case 7: print("July")
#     case 8: print("Aug")
#     case 9: print("Sep")
#     case 10: print("October")
#     case 11: print("Nov")
#     case 12: print("Dec")
#     case _: print("Wrong Input:") 
