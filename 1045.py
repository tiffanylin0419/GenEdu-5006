s=input()
if s.isdigit():
    print(s,"is a number.")
elif s.isupper():
    print(s,"is a capital letter.")    
elif s.islower():
    print(s,"is a lowercase letter.")
    print("swap to capital letter ",s.upper(),".",sep="")
else:
    print(s,"is a punctuation.")






