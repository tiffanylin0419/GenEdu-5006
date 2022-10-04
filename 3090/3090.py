import os
file1 = open('./app/math_list.csv', 'r',encoding="big5")
file2 = open('./app/english_list.csv', 'r',encoding="big5")

data1=file1.readlines()
file1.close()
data2=file2.readlines()
file2.close()

data11=set()
for i in data1[1:]:
    data11.add(i[0:9])
data22=set()
for i in data2[1:]:
    data22.add(i[0:9])


d1=data11.intersection(data22)
d5=data11.union(data22)
d3=data11-d1
d4=data22-d1
d2=d3.union(d4)

d1=list(d1)
d2=list(d2)
d3=list(d3)
d4=list(d4)
d5=list(d5)

d1.sort()
d2.sort()
d3.sort()
d4.sort()
d5.sort()


print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

