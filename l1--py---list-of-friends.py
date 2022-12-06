from os import system
system("cls")

friends = ["Anna", "Larisa"]

while len(friends) < 10:
    name = input("Add friend name: ")
    if name == "":
        break
    elif name in friends :
        print ("Numele se repeta") 
        friends.remove(name)
        

    friends.append(name)

print ("you have", len(friends), "friends")
for i in range (len(friends)):
    print( "   ",i,">>",  friends[i])
