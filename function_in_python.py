# 1. Function to find geometric mean
def calculateMean(a, b):
    mean = (a+b)/2
    print("Mean of ", a, " and ", "b", " is ", mean)

a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))
calculateMean(a, b)

# 2. Find which no. is greater
def greater(a, b):
    if(a > b):
        print(a, " is greater than ", b)
    else:
        print(b, " is greater than ", a)
greater(a, b)