import math
s=input()
c=0
while s != "q":
    if s[len(s)-1].isdigit():
        c+=float(s)-math.floor(float(s))
    s=input()
print("%.2f"%(c))
        
    
