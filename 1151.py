a=[]
n=input()
while n != "-1":    
    a.append(int(n))
    n=input()
for i in range(len(a)):
    print(a[len(a)-1-i])
    print("\n"*a[len(a)-1-i],end="")
print("-"*20)
