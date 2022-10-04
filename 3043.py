num=input().split()
num[0]=0
num[len(num)-1]=0
num=list(map(int,num))
time=0
for i in range(len(num)-1):
    if num[i+1]-num[i]==0:
        time+=5
    elif num[i+1]>num[i]:
        time+=10*(num[i+1]-num[i])
    else:
        time+=6*(num[i]-num[i+1])
print(time)
