def BD_Construction(MatrixA,District):
    for i in range(len(MatrixA)):
        for j in range(len(MatrixA[i])):
            MatrixA[i][j]=int(MatrixA[i][j])
    count=0
    for i in MatrixA:
        count+=sum(i)
    if count<9:
        return 'None'
    else:
        ss=''
        xx=[]
        yy=[]
        ss+='District-'+District+'\n'
        x=0
        y=0
        for i in range(len(MatrixA)-1,-1,-1):
            for j in range(len(MatrixA[i])):
                if MatrixA[i][j]==1:
                    x,y=i,j
                    break
        xx.append(x)
        ss+='N('+str(x)+','+str(y)+')\n'
        x=0
        y=0
        for i in range(len(MatrixA)):
            for j in range(len(MatrixA[i])-1,-1,-1):
                if MatrixA[i][j]==1:
                    x,y=i,j
                    break
        xx.append(x)
        ss+='S('+str(x)+','+str(y)+')\n'
        x=0
        y=0
        for j in range(len(MatrixA[i])-1,-1,-1):
            for i in range(len(MatrixA),):
                if MatrixA[i][j]==1:
                    x,y=i,j
                    break
        yy.append(y)
        ss+='W('+str(x)+','+str(y)+')\n'
        x=0
        y=0
        for j in range(len(MatrixA[i])):
            for i in range(len(MatrixA)-1,-1,-1):
                if a[i][j]==1:
                    x,y=i,j
                    break
        yy.append(y)
        ss+='E('+str(x)+','+str(y)+')\n'
    if count>15:
        
        ss+='Command center('+str(round(sum(xx)/2+0.1))+','+str(round(sum(yy)/2+0.1))+')\n'
    return ss

a=[]
s=input()
while s[0].isdigit():
    a.append(s.split())
    s=input()
ss=BD_Construction(a,s)
print(ss,end='')

