from collections import Counter
t=int(input())
n=t
w=[]
l=[]
while(n):
    a,b=map(int,input().split())
    w.append(a)
    l.append(b)
    n-=1 
win=[]
lose=[]
c=Counter(l)
for i in range(t):
    if(c[w[i]]==0):
        win.append(w[i])
    if(c[w[i]]==1):
        lose.append(w[i])
    if(c[l[i]]==1):
        lose.append(l[i])
win=sorted(list(set(win)))
lose=sorted(list(set(lose)))
print(*win)
print(*lose)
