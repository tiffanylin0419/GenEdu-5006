key=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
val=[]
for i in range(26):
    val.append(i+1)
d = dict(zip(key, val)) 
num=int(input())
a=[]
c=[]
count=0
for i in range(num):
    s=input()
    s=s.upper()
    a.append(s)
    for j in s:
        count+=d[j]
    print(s,"=",count)
    c.append(count)
    count=0
n=0
ss=""
for i in range(num):
    if c[i]>n:
        n=c[i]
        ss=a[i]
    elif c[i]==n:
        if ss>a[i]:
            n=c[i]
            ss=a[i]
    
print(ss,"is the key.")
