f = open('myFile.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break