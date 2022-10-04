num=int(input())
x1=[]
y1=[]
for i in range(num):
    word=input()
    x,y=word.split(" ",maxsplit=1)
    x1.append(x)
    y1.append(y)
d=dict(zip(x1,y1))
        
n=int(input())
for i in range(n):
    s1=set()
    s2=set()
    wordb,wordc=input().split()
    no,w1=d[wordb].split(" ",maxsplit=1)
    no,w2=d[wordc].split(" ",maxsplit=1)
    for j in w1.split():
        s1.add(j)
    for j in w2.split():
        s2.add(j)
    ingre=s1.intersection(s2)
    ll=[]
    for j in ingre:
        ll.append(j)
    ll.sort()
    if ingre:
        k=0
        for j in ll:
            if k !=0:
                print("",j,end="")
            else:
                print(j,end="")
            k+=1
        print()
    else:
        print("nothing")
            
                   
