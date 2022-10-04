word=input()
s=""
for i in range(len(word)):
    s=s+word[len(word)-i-1]
l=len(s.split(";"))
for i in range(l-1):
    ss,s=s.split(";",1)
    print(ss,end=" ")

print(s,end="")


