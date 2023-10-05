def fun(s,k):
    l=len(s)
    if l%k != 0:
        return "Invalid String"
    b=l//k
    p=[]
    for i in range(0,l,b):
        res=s[i:i+b]
        p.append(res)
    p=' '.join(p)
    return p
s = input()
k = int(input())
res= fun(s, k)
print(res)
