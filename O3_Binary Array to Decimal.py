n=int(input())
l=list(map(int,input().split()))
s=""
for i in l:
    s+=str(i)
print(int(s,2))
