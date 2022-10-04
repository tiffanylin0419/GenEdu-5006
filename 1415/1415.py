import math
filename=input()
file = open("./1415/"+filename, 'r')
data=file.readlines()
file.close()
people=[]
for i in data:
    i=i.split(",")
    try:
        if int(math.sqrt(int(i[1]))*11<60):
            people.append(int(i[0]))
    except:
        print("",end="")
people.sort()
for i in range(len(people)):
    if i!=(len(people)-1):
        print(people[i],end=" ")
    else:
        print(people[i])
    

