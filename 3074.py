import os
num=int(input())
if os.path.exists('files'):
    dirs = os.listdir('files')
    for file in dirs:
        os.rmdir('files/'+file)
    os.rmdir('files')

    
os.mkdir('files')
for i in range(num):
    s='files/f'+str(i+1)
    os.mkdir(s)

dir=os.listdir('files')
dir.sort()
print(dir)
os.rename('files/f1', 'files/folder1')
dir=os.listdir('files')
dir.sort()
print(dir)
os.rmdir('files/folder1')
dir=os.listdir('files')
dir.sort()
print(dir)

for file in dir:
    os.rmdir('files/'+file)

os.rmdir('files')
