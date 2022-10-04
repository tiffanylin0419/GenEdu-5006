num=int(input())
count=1
for i in range(num+1):
    for j in range(i):
        print(count,end=" ")
        count+=1
    if i!=0:
        print()
        
