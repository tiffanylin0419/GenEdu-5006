
def swap(lst):
    lst[0],lst[1]=lst[1],lst[0]
    
a=int(input())
b=int(input())
lst=[a,b]
swap(lst)
for i in lst:
    print(i)
