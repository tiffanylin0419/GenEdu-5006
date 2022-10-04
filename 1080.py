class Pokemon:
    def __init__(self,name,level,hp):
        self.Name = name
        self.Lv = level
        self.Hp = hp
    def displayProperty(self):
        print("Name:",self.Name)
        print("Lv:",self.Lv)
        print("HP:",self.Hp)
n=int(input())
p=[]        
for i in range(n):
    a=input()
    b=int(input())
    c=int(input())
    p.append(Pokemon(a,b,c))
m=int(input())
if m==0:
    for i in range(n):
        p[i].displayProperty()
        print()
elif m==1:
    num=[]
    name=[]
    for i in range(n):
        name.append(p[i].Name)
        num.append(i)
    for i in range(n-1,0,-1):
        for j in range(i):
            if name[j]>name[j+1]:
                name[j],name[j+1]=name[j+1],name[j]
                num[j],num[j+1]=num[j+1],num[j]
    for i in num:
        p[i].displayProperty()
        print()
elif m==2:
    num=[]
    lv=[]
    for i in range(n):
        lv.append(p[i].Lv)
        num.append(i)
    for i in range(n-1,0,-1):
        for j in range(i):
            if lv[j]>lv[j+1]:
                lv[j],lv[j+1]=lv[j+1],lv[j]
                num[j],num[j+1]=num[j+1],num[j]
    for i in num:
        p[i].displayProperty()
        print()
elif m==3:
    num=[]
    hp=[]
    for i in range(n):
        hp.append(p[i].Hp)
        num.append(i)
    for i in range(n-1,0,-1):
        for j in range(i):
            if hp[j]>hp[j+1]:
                hp[j],hp[j+1]=hp[j+1],hp[j]
                num[j],num[j+1]=num[j+1],num[j]
    for i in num:
        p[i].displayProperty()
        print()
    

'''

count=0    
for i in range(n):
    if p[i].Lv>p[count].Lv:
        count=i

p[count].displayProperty()
    
'''
