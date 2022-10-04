def return2num(n=0):
    n1=1
    n2=0
    for i in range(n):
        n1*=i+1
        n2+=i+1
    return n1,n2


num=int(input())
n1,n2=return2num(num)
print(n1)
print(n2)
