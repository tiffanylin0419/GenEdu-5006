d = dict(zip(('T','H','B'), ( 'Top', 'Hoodie','Backpack')))
s=input()
while s!="-1":
    l=[]
    for key in d:
        l.append(key)
    if s=="-2":
        print("keys: ",end="")
        l.sort()
        print(l)
        ll=[]
        for key in l:
            ll.append(d[key])
        print("values: ",end="")
        print(ll)
    elif s=="-3":
        s=input()
        if s in l:
            del d[s]
        else:
            print("key",s,"does not exist, cannot delete.")
        l=[]
        for key in d:
            l.append(key)
    elif s in l:
        print(d[s])
    else:
        print(s,"does not exist. Enter a new product category:")
        d[s]=input()

    s=input()
        
