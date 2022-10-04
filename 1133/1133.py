filename=input()

file = open("1133/"+filename, 'r')
data=file.readlines()
file.close()
num=[0,0,0,0,0]
lst=["PISTOL","SMG","SHOTGUN","AR","SNIPER"]
for i in data:
    for j in range(len(lst)):
        if lst[j] in i:
            num[j]+=1

for i in range(len(num)):
    if i != (len(num)-1):
        print(num[i],end=" ")
    else:
        print(num[i])
