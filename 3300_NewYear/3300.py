import os

#os.remove("./Ingredients.txt")
s1=input()
s2=input()

s1='./Amounts/'+s1
s2='./Ingredients/'+s2
file1 = open(s1, 'r', encoding='UTF-8')
num=file1.read()
file1.close()
num=[int(i) for i in num.split()]

file2 = open(s2, 'r', encoding='UTF-8')
food=file2.readlines()
file2.close()
file3 = open('./Ingredients.txt', 'w', encoding='UTF-8')
for i in food:
    i=i.split()
    file3.write(i[0]+' '+str(int(i[1])*sum(num))+'\n')
file3.close()

file4 = open('./Ingredients.txt', 'r', encoding='UTF-8')
food=file4.readlines()
file4.close()
for i in food:
    print(i,end="")
