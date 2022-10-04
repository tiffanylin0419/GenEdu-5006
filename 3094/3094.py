import os
file = open("../app/score.csv",'r')
data=file.readlines()
file.close()

s1=set()
s2=set()
s3=set()
s4=set()

for i in range(len(data)):
    if i!=0:
        d=data[i].split(",")
        s4.add(d[0])
        if int(d[1])>=60:
            s1.add(d[0])
        if int(d[2])>=60:
            s2.add(d[0])
        if int(d[1])>=60 and int(d[2])<60:
            s3.add(d[0])

l1=list(s1)
l1.sort()
l2=list(s2)
l2.sort()
l3=list(s3)
l3.sort()


print(l1)
print(l2)
print(l3)
print(len(s4))

