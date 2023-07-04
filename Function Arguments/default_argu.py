def average(a=9, b=1):
    print("The average = ", (a+b)/2)
average()
average(1,5)

# Now it will take default values as 1 and 5. 
# We can also give only one value too.

average(10)  #The another value of 2nd argument will be by default take as b = 1
average(b = 9)