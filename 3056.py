num1,num2=map(int,input().split())
count=0
for i in range(num1,num2+1):
    if i%7==0 and count==0:
        print(i,end="")
        count+=1
    elif i%7==0:
        print(" &",i,end="")
print()
count=0
for i in range(num1,num2+1):
    if "7" in str(i)and count==0:
        print(i,end="")
        count+=1
    elif "7" in str(i):
        print(" &",i,end="")
print()    
