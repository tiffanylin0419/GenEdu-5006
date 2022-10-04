n,x,y=map(int,input().split())
if n%2==1:
    temp=20+(n//2+1)*x-(n//2)*y
else:
    temp=20+(n//2)*x-(n//2-1)*y
print(temp)
