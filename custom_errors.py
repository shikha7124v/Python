a = int(input("Enter any value between 3 to 5: "))

if(a<3 or a>5):
    raise ValueError("Error!! Value should be between 3 and 5.")

# Defining Custom Exceptions 
'''In python we can define custome exceptions by creating a new class that is defined from the buit in Exception class'''

'''
class CustomeError(Exception):
    pass
try:
    # code
except CustomeError:
    # code
'''