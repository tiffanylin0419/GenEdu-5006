s=input()
while s!="-1":
    s1=s+"."
    s1=s1.replace("p","q")
    s1=s1.replace("b","d")
    s2=""
    for i in range(len(s)):
        if s[i]=="d":
            s2+="b"
        elif s[i]=="q":
            s2+="p"
        else:
            s2+=s1[i]

    print(s2)
    s=input()

