import math
num=int(input())
word=input()
a=[]
for i in word.split():
    a.append(int(i))
if num%2==0:
    code=math.ceil((a[int(num/2)]+a[int(num/2)-1])/2)
else:
    code=a[int(num/2)]
print(code)
