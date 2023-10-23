l=list(map(int,input().split()))
k=int(input())
p=[]
n=len(l)
for i in range(k):
    p.append(l[i])
    p.append(l[k+i])
print(*p)
