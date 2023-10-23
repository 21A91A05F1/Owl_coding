l=list(map(str,input().split()))
c=0
for i in l:
    if i=="X++" or i=="++X":
        c+=1 
    else:
        c-=1 
print(c)
