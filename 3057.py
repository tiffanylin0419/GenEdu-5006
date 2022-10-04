def Matrix_Inverse(MatrixA):
    a=[[float(MatrixA[0][0]),float(MatrixA[0][1])],[float(MatrixA[1][0]),float(MatrixA[1][1])]]
    det=a[0][0]*a[1][1]-a[1][0]*a[0][1]
    if det==0:
        print('none')
        return
    A_1=[[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]
    
    for i in range(2):
        for j in range(2):
            A_1[i][j]=round(A_1[i][j]+0.001,1)
    print(A_1[0][0]," ",A_1[0][1],"\n",A_1[1][0]," ",A_1[1][1],sep="")   
    return


s1=input().split()
s2=input().split()
a=[s1,s2]
Matrix_Inverse(a)

