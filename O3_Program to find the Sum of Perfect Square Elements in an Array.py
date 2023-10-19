import math
def is_perfect(n):
    a=math.sqrt(n)
    if((a)*(int)(a)==n):
        return 1
    return 0 
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if is_perfect(i):
        s+=i 
print(s)
