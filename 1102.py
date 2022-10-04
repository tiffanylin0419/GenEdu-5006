n=int(input())
m=int(input())
for i in range(n):
    for j in range(m):
        print(i+1,"*",j+1,"=","%2d"%((i+1)*(j+1)),sep="",end=" ")
    print("")
