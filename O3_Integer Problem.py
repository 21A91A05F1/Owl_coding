def fun(a, b):
    diff = abs(a - b)
    return (diff + 9) // 10
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(fun(a,b))
