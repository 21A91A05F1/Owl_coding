def fun(n):
    c=0
    for a in range(1, n):
        if n % a == 0:
            b = n // a
            if a < b:
                c += 1
    return c
n=int(input())
print(fun(n))
