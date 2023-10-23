n=int(input())
l=list(map(int,input().split()))
p,k=[],[]
for i in l:
    if i<0:
        p.append(i)
    else:
        k.append(i)
print(*(p+k))
