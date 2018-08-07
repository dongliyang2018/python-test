names = [ "Tom", "Jerry", "Jim" ]
print("Welcome " + str(names))

print("Jim can't come here")
names[2] = "Lily"
print("Welcome " + str(names))

print("I found a big table")
names.insert(0,"John")
names.insert(2,"Peter")
names.append("Wong")
print("Welcome " + str(names))
print("only two")
del_name = names.pop()
print("sorry,delete from list " + del_name)
del_name = names.pop()
print("sorry,delete from list " + del_name)
del_name = names.pop()
print("sorry,delete from list " + del_name)
del_name = names.pop()
print("sorry,delete from list " + del_name)
print(names)
print(names[0] + " still in list")
print(names[1] + " still in list")
del names[0]
del names[0]
print(names)
