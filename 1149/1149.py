filename=input()

file = open("1149/"+filename, 'r')
data=file.readlines()
file.close()

for i in range(len(data)):
    if i==0:
        continue
    d=data[i]
    score=0
    d=d.split(',')
    score=0.7*(int(d[1])+int(d[2])+int(d[3])+int(d[4]))/4+0.3*int(d[5])*2.5
    if score <60 and int(d[5])==40:
        score=60
    print(d[0],"%.2f"%score)
