s1=input()
s2=input()
n,k=s1.split()
n,k=int(n),int(k)
fish=[]
for i in s2.split():
    fish.append(int(i))
count=0
for i in range(n):
    if fish[i]>=k:
        count+=k*(fish[i]//k)
print(count)
    


