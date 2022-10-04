class Data:
    Animal_list=dict()
    animal=[]
    def __init__(self):
        scientific_name = ''
        number = 0
    def add(self,name,num):
        Data.animal.append(name)
        self.scientific_name=name
        self.number=num
        print('Add. Animal: ',self.scientific_name,'.',sep="")
        print('Number:',self.number)
        Data.Animal_list[name]=num
        if self.number<1000:
            print('Endanger species: Yes')
        else:
            print('Endanger species: No')

    def update(self,num):
        self.number=num
        print('Update. Animal: ',self.scientific_name,'.',sep="")
        print('Number:',self.number)
        Data.Animal_list[self.scientific_name]=num
        if self.number<1000:
            print('Endanger species: Yes')
        else:
            print('Endanger species: No')
            
    def display():
        i=0
        for value in Data.Animal_list.values():
            if value<1000:
                i+=1
        print('There are',i,'animals who are endanger species')
        
        for i in Data.animal:
            if Data.Animal_list[i]<1000:
                print ('Animal: ',i,'.',sep="")
                print ('Number:',Data.Animal_list[i])
        
        
            

s=input().split(maxsplit=1)
p=[]
while s[0]!='q':
    if s[0]=='a':
        num=int(input())
        temp=Data()
        temp.add(s[1],num)
        p.append(temp)
    elif s[0]=='u':
        num=int(input())
        for i in range(len(p)):
            if p[i].scientific_name==s[1]:
                p[i].update(num)
    elif s[0]=='d':
        Data.display()
    s=input().split(maxsplit=1)
print('That are the endanger animal list we have now. Bye bye.')
