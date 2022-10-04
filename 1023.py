num=int(input())
s=input()
a=[]
for i in s.split():
    a.append(i)

x1=0
y1=int(a[0])
x2=0
y2=int(a[0])

for i in range(num):
    if y1<int(a[i]):
        y1=int(a[i])
        x1=i
    if y2>int(a[i]):
        y2=int(a[i])
        x2=i
print(x1+1,y1)
print(x2+1,y2)
