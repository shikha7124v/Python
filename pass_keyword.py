# Without writting the body of any function and running it as it is will throw error
# Do stop throwing error with the use of pass keyword 
# Pass means i'll write this function later and there's no need for python to search for anything 
# Pass means "Pass and Process next"

def isGreater(a, b):
    if(a > b):
        print("True")
    else:
        print("False")
def isLesser(a, b):
    pass

a = 9
b = 3
isGreater(a, b)