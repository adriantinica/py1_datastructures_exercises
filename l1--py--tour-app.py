
#HW1:

# use for inside for to write all the destinations\
# make the result to look like this:
# America:
#     "New York"
#     "Ottawa"
#     ...
# Romania:
#     "Bucharest"
#     .....
      

from os import system
system("cls")

destinations =[[ "New York","Ottawa","Los Angeles" ] , [ "Bucharest","Brasov","Cluj Napoca"]  ]

#print (destinations)
for i in range(len(destinations)):
    if i == 0:
        print("America:" )
    else: 
        print("Romania:" )
    for j in range(len(destinations[i])):
       print(j+1,destinations[i][j])


