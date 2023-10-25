n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(n):
    if(len(p)==n):
        break
    if(l[i]==0):
        p.append(0)
        p.append(0)
    else:
        p.append(l[i])
print(*p)
