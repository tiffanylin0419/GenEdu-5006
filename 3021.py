score=int(input())
if score<60:
    gpa=0
    str="F"
elif score<63:
    gpa=1.7
    str="C-"
elif score<67:
    gpa=2.0
    str="C"
elif score<70:
    gpa=2.3
    str="C+"
elif score<73:
    gpa=2.7
    str="B-"
elif score<77:
    gpa=3.0
    str="B"
elif score<80:
    gpa=3.3
    str="B+"
elif score<85:
    gpa=3.7
    str="A-"
elif score<90:
    gpa=4.0
    str="A"
else:
    gpa=4.3
    str="A+"

print(gpa)
print(str)
    
