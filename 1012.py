school=int(input())
if school==1:
    grade=int(input())
    if grade>100 or grade<0:
        print("score error")
    elif grade<60:
        print("fail")
    else:
        print("pass")
elif school==2:
    grade=int(input())
    if grade>100 or grade<0:
        print("score error")
    elif grade<70:
        print("fail")
    else:
        print("pass")    
else:
    print("role error")
