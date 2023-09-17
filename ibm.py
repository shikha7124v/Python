import array
def table(*num):
    for i in num:
        n = num
        for j in range(1, n+1):
            print(n,"*",j,"=",n*j)
table(2, 3)