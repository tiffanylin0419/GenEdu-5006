ints,floats=[],[]
i=input()
x,y=1,1
while i!="q":
    i=float(i)
    if i%1==0:
        ints.append(int(i))
    else:
        floats.append(i)
    i=input()
        
for i in ints:
    x*=i
for i in floats:
    y*=i
print("%.2f"%y)
print(x)
if y-x>0:
    symbol=">"
elif y-x<0:
    symbol="<"
else:
    symbol="="
print("Float",symbol,"Int")

