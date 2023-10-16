def fun(arr):
    odd = set()
    for i in arr:
        if i % 2 ==1:
            odd.add(i)
    return sum(odd)
n= int(input())
a= list(map(int, input().split()))
res = fun(a)
print(res)
