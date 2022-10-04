num=int(input())
x1,x2=input().split()
x1,x2=int(x1),int(x2)
a=[]
for i in range(num):
    a.append(0)
a[x1-1]=1
a[x2-1]=2
print(a)

n=int(input())
while n!=-1:
    if x1<x2:
        if n<x1:
            x1=n
        elif n>x2:
            x2=n
        else:
            if x2-n<n-x1:
                x2=n
            else:
                x1=n
    else:
        if n<x2:
            x2=n
        elif n>x1:
            x1=n
        else:
            if x1-n<n-x2:
                x1=n
            else:
                x2=n
    a=[]
    for i in range(num):
        a.append(0)
    a[x1-1]=1
    a[x2-1]=2
    print(a)
    n=int(input())
