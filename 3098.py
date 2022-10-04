num1=input()
num2=0
count=0
while num1!="q":
    if num1=="1":
        num2=input()
        if num2=="q":
            break
        elif num2=="9":
            count+=1
            num1=num2
        else:
            num1=num2
    else:
        num1=input()
print(count)
