dic = {
    'name' : 'Shikha',
    'roll' : 18,
    'eligible' : True
}
print(dic)
print(type(dic))

print(dic.keys())

ep1 = {
    101 : 10,
    102 : 11,
    103 : 12
}
ep2 = {
    104 : 13,
    105 : 14
}
ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)

dic.pop('roll')
print(dic)

# function popitem() delets the last key value pair automatically 

dic.popitem()
print(dic)

# del keyword is for delete 

del ep1 #it will delete the dep1 dictionary

del ep2[104] #it will only delete the key 104 value pair from the ep1 dictionary

