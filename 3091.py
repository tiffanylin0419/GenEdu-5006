class student:
    #name
    #gender
    grades=[]
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
    def avg(self):
        return sum(self.grades)/len(self.grades)
    
    def add(self,grade):
        self.grades.append(grade)

    def fcount(self):
        num=0
        for i in self.grades:
            if i<60:
                num+=1
        return num

    def show(self):
        print(self.name)
        print("%.2f"%self.avg())
        print(self.fcount())
name=input()
gender=input()
s=student(name,gender)
for i in range(3):
    grade=int(input())
    s.add(grade)

s.show()
