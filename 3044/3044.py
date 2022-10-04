import os
name=input()
file = open(name, 'r')
data=file.readlines()
file.close()

r=0
e=0
for i in data:
    i=i.split(",")
    if i[3]!="F\n":
        if i[1]=="R":
            r+=int(i[2])
        elif i[1]=="E":
            e+=int(i[2])
print("Required:",r)
print("Elective:",e)
if r>=72 and e>=28:
    print("Y")
elif r<72 and e>=28:
    print("N")
    print("Student still needs to complete",72-r,"required credits for graduation.")
elif r>=72 and e<28:
    print("N")
    print("Student still needs to complete",28-e,"elective credits for graduation.")
else:
    print("N")
    print("Student still needs to complete",72-r,"required credits &",28-e,"elective credits for graduation.")
