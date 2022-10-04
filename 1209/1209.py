import os
file = open("./stores_old.csv", 'r', encoding='big5')
data=file.readlines()
file.close()

if "stores_new.csv" in os.listdir():
    os.remove("./stores_new.csv")
    
fileo = open("./stores_new.csv", 'a', encoding='UTF-8')



ar=[0,3,5,6]
for i in data:
    s=""
    i=i.split(',')
    for j in ar:
        s=s+i[j]+","
    fileo.write(s[:])
    fileo.write("\n")

fileo.close()


fileo = open("./stores_new.csv", 'r', encoding='UTF-8')
data=fileo.readlines()
for i in data:
    print(i,end="")

fileo.close()
