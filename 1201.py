inn=input( ).split( )
a,b=int(inn[0]),int(inn[1])

y=(b-2*a)/2
x=2*a+-b/2

if x<=0 or y<=0:
    print("NO",end='')
elif x%1==0 and y%1==0:
    print("YES")
    print(int(x),int(y),end='')
else:
    print("NO",end='')

