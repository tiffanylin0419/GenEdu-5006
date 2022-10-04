def dd(num):
    a=1
    for i in range(num):
        a*=(i+1)
    return a

def P(n,m):
    if n>=m:
        return round(dd(n)/dd(n-m))
    return 0


def C(n,m):
    if n>=m:
        return round(P(n,m)/dd(m))
    return 0



