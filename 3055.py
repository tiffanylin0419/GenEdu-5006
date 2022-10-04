def ch(num):
    a=num//26
    b=num%26
    if b==0:
        b=26
        a-=1
    print(chr(b+96)*(a+1),end="")

nums=input().split('-')
for i in nums:
    ch(int(i))


