n=int(input())
for i in range(0,n):
    a=(n-2*i)
    if(a%7==0):
        print("YES")
        break 
else:
    print("NO")
