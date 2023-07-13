# Exception Handling is the process of responding to unwanted and unexpected events when a computer program runs.
# Exception Handling deals with these events to avoid the program and system chrashing.
# Python has many built-in exceptions that are raised when your program encounters an error something is program goes wrong.
# When these excpetions occur, the python interpreter stops the current process and passes it to the calling process until it is handled.
# If not handled, the program will crash. 

'''
a = input("Enter a number : ")
print(f"Multiplication table of {a}")

try:
    for i in range(1,11):
        print(f"{int(a)} * {int(i)} = {int(a*i)}")

except:
    print("Exception Occured")

print("If you will try to enter input other than interger or float then except will occur")
'''

try:
    num = int(input("Enter a number: "))
    a = [1,2]
    print(a[num])
except ValueError:
    print("No. entered is not an integen Value Error !!")
except IndexError:
    print("Index Error !!")
