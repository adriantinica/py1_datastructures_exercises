
from os import system
system("cls")


# one waiter -> 3 tables

food_name   = ["Pizza", "Pasta", "Salad"]
food_prince = [ 120.00,   55.00,   45.00] 

status =[ "free", "free", "free"] 
client =[     "",     "",     ""]
order  =[     "",     "",     ""]
bill   =[  00.00,  00.00,  00.00]  
tip    =[  00.00,  00.00,  00.00]  


#john ordered a salad


print(f"Astazi in meniu {food_name}")
client[2] = "John"
status[2] = "occupied"

client[1] = "Marry"
status[1] = "ocuppied"

client_name = "John"
food_ordered_name = "Salad"



client_idx = client.index(client_name)
order[client_idx] = food_ordered_name
food_idx = food_name.index(food_ordered_name)
bill[client_idx] = food_prince[food_idx]
tip[client_idx] = bill[client_idx] / 10


for ti in range (len(status)):
    print(f"table {ti+1} {status[ti]}")
    if status[ti] != "free":
        print(f"\t {client[ti]}")
        if order[ti] == "":
            quit
        else:
            print(f"\t {order[ti]} -> {bill[ti]} % {tip[ti]}")

