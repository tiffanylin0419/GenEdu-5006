s=input().lower()
def change(c):
    n=3
    if c.isalpha():
        if ord(c)<ord("a")+n-1:
            c=chr(ord(c)-n+26)
        else:
            c=chr(ord(c)-n)

    
    return c
j=0
while s!="-1":
    ss=""
    for i in s:
        ss+=change(i)
    if j==0:
        print(ss,end="")
    else:
        print("",ss,end="")
    s=input().lower()
    j+=1
