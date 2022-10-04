def matrixMultiPly(a, b) :
    c=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            total=0
            for k in range(3):
                total+=int(a[i][k])*int(b[k][j])
            c[i][j]=total

    return c
    
a=[[],[],[]]
for i in range(3):
    a[i]=input().split()

b=[[],[],[]]
for i in range(3):
    b[i]=input().split()

c=matrixMultiPly(a, b)
for i in c:
    print(i)
    

