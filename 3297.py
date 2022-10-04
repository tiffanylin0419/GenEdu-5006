H=int(input())
while H<=1:
    print('Please enter a height greater than 1')
    H=int(input())

c=input()
if c=='Y':
    out=input()
    while len(out)>1:
        print('Please enter only one character!')
        out=input()
    for i in range(H):
        left=H-i-1
        right=2*i
        print(' '*left,'/',' '*right,'\\',sep="")
    mid=H-2
    print('|',' '*mid,out.upper(),'+',' '*mid,'|',sep="")    
    for i in range(H-1,-1,-1):
        left=H-i-1
        right=2*i
        print(' '*left,'\\',' '*right,'/',sep="")     
else:
    for i in range(H):
        left=H-i-1
        right=2*i
        print(' '*left,'/',' '*right,'\\',sep="")
    
    for i in range(H-1,-1,-1):
        left=H-i-1
        right=2*i
        print(' '*left,'\\',' '*right,'/',sep="")      


    
