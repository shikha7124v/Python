# Opening a file 
f = open('myFile.txt', 'r')
'''Python provides the open() function to open a file. It takes two agruments: the name of 
the file and the mode in which the file should be opened, such as 'r' for reading 'w' for 
writting or 'a' for appending '''
print(f)
text = f.read()
print(text)
f.close()


