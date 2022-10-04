n1=float(input())
n2=float(input())
symbol=input()
if symbol=="+":
    num=n1+n2
elif symbol=="-":
    num=n1-+n2
elif symbol=="*":
    num=n1*n2
elif symbol=="/":
    num=n1/n2
print("%.2f"%n1,symbol,"%.2f"%n2,"=","%.2f"%num)
