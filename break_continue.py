# The break statement enables a program to skip over a part of the code.
# A break statement termnates the very loop it lies within.

for i in range(12):
    if(i == 10):
        break
    print("5 * ",i+1,"=",5*(i+1))
print("Out of loop")

# Continue statement skips the rest of the loop statement and causes the next iteration to occur 

for j in range(12):
    if(j == 10):
        print("Skips the 10th iteration")
        continue
    print("5 * ",j,"=",5*j)