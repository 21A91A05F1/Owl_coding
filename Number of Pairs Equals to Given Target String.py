n=int(input())
arr=list(map(str,input().split()))
t=input()
c=0
for i in range(n):
    for j in range(n):
        if(arr[i]+arr[j]==t):
            c+=1
print(c)
