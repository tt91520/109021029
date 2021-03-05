def fun(n):
    if n < 10:
        return 1
    else:
        return 1 + fun(n // 10)
print(int(input()))


def funya(m,n):
    if m % n == 0:
        return n
    else:
        return fun(n, m % n)


def fun2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fun(n - 1) + fun(n - 2)
print(fun(int(input())))
    

def ge(a):
    b = 1
    for i in range(a,1,-1):
        b = b * i
    return
    
    