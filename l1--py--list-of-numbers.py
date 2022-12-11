from os import system
system("cls")

list = [10, 3, -12, 20, 25, 30, 75]

#len
print (f"The list has {len(list)} items")

half_idx = round(len(list)/2)
# set zeros in the second half of the list


# print(half_idx)

# for i in range(half_idx, len(list)):
#     list[i]=0
# print(list)


# set zeros in the first half of the list


#for i in range(0, half_idx):
#    list[i]=0
#print(list)



#3 swaping 
#print(list)
#print()
#idx_1 = int(input("First idx you want to switch (from 0 to 6): "))
#idx_2 = int(input("Second idx you want to switch (from 0 to 6): "))
#print()

#free = list[idx_1]
#list[idx_1] = list[idx_2]
#list[idx_2] = free

#print(list)

# hw3: find the max and min items and print them:
print()
val_max = max(list)
print(f"The val max is {val_max} in that list")
print()
val_min = min(list)
print(f"The val min is {val_min} in that list")
print()
idx = val_max
found_idx = list.index(idx)

print(f"The {val_max} is on {found_idx} position in list")
print()
idx = val_min
found_idx = list.index(idx)

print(f"And the {val_min} is on {found_idx} position in list")
print()



