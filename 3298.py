d={'ST': 'BEP1155,001', 'MFB': 'BEP1155,002', 'CCC': 'BEP1155,003'}
do=input()
while do!='-1':
    if do=='q':
        key=list(d.keys())
        key.sort()
        val=[]
        for i in key:
            val.append(d[i])
        print('keys:',key)
        print('values:',val)
    elif do=='-d':
        do=input()
        try:
            del d[do]
        except:
            print('key',do,'does not exist, cannot delete.')
    else:
        try:
            print(d[do])
        except:
            print(do,'does not exist. Enter a new art project：')
            art=input()
            d[do]=art
    do=input()

