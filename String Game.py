t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=[]
    c=0
    for i in set(s):
        l.append(s.count(i))
    for i in l:
        if i%2!=0:
            c=1
            break
    if c==0:
        print("YES")
    else:
        print("NO")
