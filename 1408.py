import sys
find=input().lower()
book=input()
i=0
while book !="q":
    book=book.lower()
    i+=1
    if book==find:
        print("Yes",end=" ")
        print(i)
        sys.exit()
    book=input()

print("No",end=" ")
print(i)
        
        
    
