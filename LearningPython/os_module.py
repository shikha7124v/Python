import os
# if(not os.path.exists("data")):
#   os.mkdir("data")

# for i in range(5):
#   os.mkdir(f"data/day{i+1}")



# for i in range(5):
#     os.rename(f"data/day{i+1}", f"data/tut{i+1}")

folders = os.listdir("data")
print(folders)

print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())   #to get the current working directory
os.chdir("/Users") #to change the dierctory