n=int(input())
l=list(map(int,input().split()))
res=[]
for i in l:
    if(l.count(i)==1):
        res.append(i)
if(len(res)):
    print(max(res))
else:
    print("-1")
