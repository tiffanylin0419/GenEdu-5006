class Pokemon:
    def Attack(self,tar):
        if self.HpCurrent==0:
            print(tar.Name,'Win,',self.Name,'Lose.')
            print(self.Name,'is unable to attack.')
        else:
            print(self.Name,'Attack',tar.Name,self.Lv,'Points.')
            tar.Defence(self.Lv)
    def Defence(self,dmg):
        self.HpCurrent-=dmg
        if self.HpCurrent<=0:
            print(self.Name,'Seriously Injured.')
            self.HpCurrent=0
    def Cure(self):
        self.HpCurrent=self.HpMax
    def setData(self,name,level,hp):
        self.Name = name
        self.Lv = level
        self.HpMax = hp
        self.HpCurrent = hp
    def ShowInfo(self):
        print("Name:",self.Name)
        print("Lv:",self.Lv)
        print("HP: ",self.HpCurrent,'/',self.HpMax,sep="")   

        
m=Pokemon()
m.setData('Mewtwo',30,300)
    
n=int(input())
p=[]        
for i in range(n):
    a=input()
    b=int(input())
    c=int(input())
    p.append(Pokemon())
    p[i].setData(a,b,c)
    print('#',i+1,sep="")
    while (True):
        p[i].Attack(m)
        if(p[i].HpCurrent==0):
            break
        m.Attack(p[i])
        if(m.HpCurrent==0):
            break
    m.ShowInfo()
    p[i].ShowInfo()
    print()
    m.Cure()
