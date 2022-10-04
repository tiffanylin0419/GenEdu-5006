num=int(input())
y,n,yn=0,0,0
for i in range(num):
    s=input()
    if s.isupper():
        n+=1
    elif s.islower():
        y+=1
    else:
        yn+=1
print(y,n,yn)
