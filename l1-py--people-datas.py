# To create an table wich will contain fisrt_name, last_name and age of people, inputed by user. 

from os import system
system("cls")

students_first_name = []
students_last_name = []
students_age = []
students_mark = []

while len(students_first_name) < 100:
    data = input("Add data divided by /: ")
    if data == "":
        break
    data_splited= data.split()

    if  int(data_splited[2]) >= 18 and int(data_splited[2]) <= 30 and int(data_splited[3])>=1 and int(data_splited[3])<=10:
        students_first_name.append(data_splited[0])
        students_last_name.append(data_splited[1])
        students_age.append(data_splited[2])
        students_mark.append(data_splited[3])
    
    
for i in range(len(students_first_name)):             
    print(i+1, students_first_name[i],students_last_name[i], students_age[i], students_mark[i])
        
print(students_mark)   