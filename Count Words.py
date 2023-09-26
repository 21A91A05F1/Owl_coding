def fun(s):
    v='aeiouAEIOU'
    c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    s=s.split()
    d=0
    for i in s:
        if i and i[0] in v and i[-1] in c:
            d+=1 
    return d
s=input()
print(fun(s))
