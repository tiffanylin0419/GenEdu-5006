score=int(input())
if score<80:
    money=0
elif score<90:
    money=500
elif score<95:
    money=1000
else:
    money=2000
print("獎金",money,"元")
