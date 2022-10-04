def YEAR(lst):
    y1=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    y2=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    for i in lst:
        a=(i-3)%10
        b=(i-3)%12
        print(i,"= %s%s年"%(y1[a-1],y2[b-1]))
        

a=input()
lst=[]
while(a!="q"):
    year=int(a)
    lst.append(year)
    a=input()
    
YEAR(lst)
