num=int(input())
d={}
for i in range(num):
    a,b=input().split()
    if a in d:
        d[a]+=int(b)
    else:
        d[a]=int(b)

c=0
for i in d:
    if d[i]>c:
        c=d[i]
        food=i
print(food,c)





