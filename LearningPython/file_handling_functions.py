# seek() and tell()
with open('myFile.txt','r') as f:
    print(f)
    f.seek(10)

    data = f.read(5)
    print(data)