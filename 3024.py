import time
sec=float(input())
t=time.gmtime(sec)
print(time.strftime("%Y-%m-%d %H:%M:%S",t))

t=time.localtime(sec)
print(time.strftime("%Y-%m-%d %H:%M:%S",t))
