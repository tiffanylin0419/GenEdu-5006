filename=input()

file = open("1204/"+filename, 'r')
data=file.readlines()
file.close()
for i in range(int(len(data)/2)):
    
    if int(data[2*i+1])>50:
        print(data[2*i].strip(),data[2*i+1].strip())
