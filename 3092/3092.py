import os
name=input()
file = open("../app/"+name, 'r')
data=file.readlines()
file.close()

total=0
people=0
for i in range(int(len(data)/2)):
    print("chef",data[2*i][:-1],data[2*i+1],end="")
    total+=int(data[2*i+1])
    people+=1
print("\nTotal:",total)
print("Avg: %.2f"%(total/people))
