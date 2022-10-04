class Pokemon:
    def __init__(self,name="No Name",lv=1,hp=1):
        if name=="":
            print("Name can't be empty.")
            name="No Name"
        self.Name = name
        if lv<1:
            print("Lv setting error.")
            lv=1
        self.Lv = lv
        if hp<1:
            print("Hp setting error.")
            hp=1
        self.HpMax = hp
        self.HpCur = hp
    def __del__(self):
        print(self.Name,'has returned to the nature.')
    def Attack(self,tar):
        if self.HpCur==0:
            print(self.Name,'is unable to attack.')
        elif tar.HpCur==0:
            print(self.Name,' cannot attack fainted target ',tar.Name,'.',sep="")  
        else:
            print(self.Name,'Attack',tar.Name,self.Lv,'Points.')
            tar.Defence(self.Lv)
    def Defence(self,dmg):
        self.HpCur-=dmg
        if self.HpCur<=0:
            print(self.Name,'is fainted.')
            self.HpCur=0
    def Cure(self):
        self.HpCurrent=self.HpMax

        
    def ShowInfo(self):
        print("Name:",self.Name)
        print("Lv:",self.Lv)
        print("HP: ",self.HpCur,'/',self.HpMax,sep="")
        print()

 
 
name = input().strip()
lv = int(input())
hp = int(input())
p1 = Pokemon(name,lv,hp)
p1.ShowInfo()
del p1
 
name = input().strip()
lv = int(input())
hp = int(input())
p2 = Pokemon(name,lv,hp)
p3 = Pokemon()
 
p2.ShowInfo()
p3.ShowInfo()
del p3
del p2
