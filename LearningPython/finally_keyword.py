# finally keyword 
'''
try:
    i = int(input("Enter a no. :"))
    a = [1,2,3]
    print(a[i])
except:
    print("Exception Occurred")
finally:
    print("Finally will occur even after the execution of except")
'''
# It executes even after returning the function 
def func():
    try:
        l = [1,4,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")
x = func()
print(x)