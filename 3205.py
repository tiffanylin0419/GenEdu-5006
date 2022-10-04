class city_and_infect:
    def __init__(self,name,people,infected): 
        self.name=name#城市名稱
        self.people=people#城市總人口數
        self.infected=infected#，城市目前被感染總人數

class virus:
    city_list=[]#型態為list，用來儲存輸入的每個城市class city_and_infect
    global_people=0#累計city_list中所有城市的總人口數
    global_infect_num=0#累計city_list中所有城市被感染的總人數
    global_infect_rate=0#累計city_list中所有城市被感染比例


    def __init__(self):
        self.total=1
    def add_city(self, city_and_infect):
        virus.city_list.append(city_and_infect)
                
        
    def infect(self, city, times, spread, separate):
        for i in virus.city_list:
            if city==i.name:
                #print(city,i.infected)
                self.total=i.infected
                for j in range(times):
                    self.total=self.total+self.total*(spread-separate)
                if self.total<i.people:
                    i.infected=self.total
                else:
                    i.infected=i.people
                print(city,'\'s infected people: ',i.infected,'/',i.people,sep="")
        
    def count(self):
        num1,num2=0,0
        for i in virus.city_list:
            num1+=i.people
            num2+=i.infected
        virus.global_people=num1
        virus.global_infect_num=num2
        virus.global_infect_rate=virus.global_infect_num/virus.global_people
    def show_detail(self):
        virus.count(self)
        print('Total:',self.global_people)
        print('current infected:',self.global_infect_num)
        print('infected rate: %.2f'%self.global_infect_rate)
        for i in virus.city_list:
            print('city name:',i.name)
            print('people num:',i.people)
            print('current infected:',i.infected)
        
Coronavirus=virus()
#print("input type")
in_str = input()
while in_str != "q":
    if in_str == "i":
        city = input()
        t, s1, s2 = [int(i) for i in input().split(" ")]
        Coronavirus.infect(city=city, times=t, spread=s1, separate=s2)
    if in_str == "a":
        name = input()
        people = eval(input())
        infected = eval(input())
        Coronavirus.add_city(city_and_infect(name=name, people=people, infected=infected))
    #print("input type")
    in_str = input()
Coronavirus.show_detail()
