filename1=input()
filename2=input()

file1 = open("../app/"+filename1, 'r')
data1=file1.read().split()
file1.close()

file2 = open("../app/"+filename2, 'r')
data2=file2.read().split()
file2.close()

data1.extend(data2)
for i in range(len(data1)):
    data1[i]=int(data1[i])
data1.sort()
for i in data1:
    print(i,end=" ")
