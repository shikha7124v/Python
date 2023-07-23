# The enumrate function is a built-in function in Python that allows you to loop over a sequence 
# (such as list, tuple, or string) and get the index and value of each element in the sequence at the same time.

marks = [12,33,43,25,67]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Awesome")
#     index += 1

index = 0
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Awesome")