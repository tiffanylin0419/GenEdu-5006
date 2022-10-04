M,N,X1,Y1,E1,N1,F1,X2,Y2,E2,N2,F2=map(int,input().split())
i=0
while True:
    i=i+1
    if F1>0:
        F1=F1-1
        if i%(E1+N1)<=N1 and i%(E1+N1)!=0:
            Y1+=1
        else:
            X1+=1
    if F2>0:
        F2=F2-1
        if i%(E2+N2)<=E2 and i%(E2+N2)!=0:
            X2+=1
        else:
            Y2+=1
    if X1%M==X2%M and Y1%N==Y2%N:
        print("robots explode at time",i)
        break
    if F1==0 and F2==0:
        print("robots will not explode")
        break

