l,s=map(int,input().split())
n=abs((s-l)//5)+2
count=abs((s-l)/2+10)
for i in range(n+1):
    j=(-l+s+5*i)/2
    if j%1==0 and i+j<count and j>=0:
        count=i+j
print(int(count))
