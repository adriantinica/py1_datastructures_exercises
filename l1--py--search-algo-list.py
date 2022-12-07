
# To identify if an element from items is or not in a container

from os import system
system("cls")


items =     ["John" , "Casandra", "Max"]
found =     [ False, False, False]
container = ["John" , "Marry" , "Casandra"]

for j in range (len(items)):
    for i in range (len(container)):
        found[j] = container[i]== items [j]
        if found[j]:
            break


for j in range (len(items)):
    if found[j]:
        print (items[j], "is in list")
    else:
        print (items[j], "is not in list")

print (found)
print (items)