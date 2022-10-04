num=input()
l=[]
while num !="q":
    if not num.isdigit():
        if num[1:].isdigit() and num[0]=="-":
            l.append(int(num))
        elif "." in num:
            l.append(float(num))
        else:
            print("Please Enter Numbers Only")
    else:
        l.append(int(num))
    num=input()
print(l)
lc=l.copy()
lc.sort()
print(lc)
lc.reverse()
print(lc)
print(l)
