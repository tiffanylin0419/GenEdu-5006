n=True
while n:
    try:
        a = eval(input())
        b = int(input())
        c = a/b
        print(a,'/',b,' = %.2f'%c,sep="")
        n=False
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
