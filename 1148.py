n,a,o,r=[],[],[],[]
t=input().split()
while t[0]!="-1":
    t[1],t[2],t[3]=int(t[1]),int(t[2]),int(t[3])
    t[1:]=sorted(t[1:])
    name,x,y,z=t
    if x+y<=z:
        n.append(name)
    elif x**2+y**2>z**2:
        a.append(name)
    elif x**2+y**2==z**2:
        r.append(name)
    elif x**2+y**2<z**2:
        o.append(name)
    t=input().split()
n,a,o,r=sorted(n),sorted(a),sorted(o),sorted(r)
nn="Not Triangle: "
aa="Acute Angle: "
oo="Obtuse Angle: "
rr="Right Angle: "

if len(n)==0:
    nn+="None"
else:
    for i in n:
        nn+=i+","
    nn=nn[:len(nn)-1]
if len(a)==0:
    aa+="None"
else:
    for i in a:
        aa+=i+","
    aa=aa[:len(aa)-1]
if len(o)==0:
    oo+="None"
else:
    for i in o:
        oo+=i+","
    oo=oo[:len(oo)-1]
if len(r)==0:
    rr+="None"
else:
    for i in r:
        rr+=i+","
    rr=rr[:len(rr)-1]

  
print(nn)
print(aa)
print(oo)
print(rr)
