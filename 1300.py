class employer:
    def __init__(self,a,b,c):
        self.ai=a
        self.bi=b
        self.ci=c
        self.mad=False
        
n=int(input())
Em=[]
for i in range(n):
    s=input().split()
    Em.append(employer(int(s[0]),int(s[1]),int(s[2])))

Em[int(input())-1].mad=True

#sort with ai
for i in range(len(Em)):
    for j in range(len(Em)-2,i-1,-1):
        if Em[j].ai<Em[j+1].ai:
            Em[j],Em[j+1]=Em[j+1],Em[j]
num=0
for i in range(len(Em)):
    if Em[i].mad:
        for j in range(i+1,len(Em)):
            if Em[j].ai<Em[i].ai and Em[j].ci<Em[i].bi:
                Em[j].mad=True
        num+=1
print(num)

