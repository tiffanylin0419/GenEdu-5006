#類別名稱
class Meta:
     
    #類別成員
    meallst = []
    profit = 0
    total = 0
     
    #類別方法(皆無回傳值，直接函式內印出相關資訊)
    def __init__(self,meal,price,c):
        self.meal=meal
        self.price=price
        self.c=c
    def a(self):
        Meta.meallst.append(self.meal)
        print('Launched! Meal: ',self.meal,'.',sep="")
        print('Price:',self.price)
'''
    def u(self,np):

        
    def s(self,sel):
        pass
    def d(self):
        pass
'''
name=input()
print('Welcome to Meta restaurant!',name)
status=input()
while status!='q':
    if status[0:2]=='-1':
        num=int(input())
        p1=Meta(status[3:],num,0)
        p1.a()
    status=input()

print('==========Meta==========')
print('Staff:',name)
print('Total Meta sold:',Meta.total)
print('Profit:',Meta.profit)
