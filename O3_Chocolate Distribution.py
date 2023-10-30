n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
mini=1e9
i=0 
j=k-1
while j<n:
    mini=min(mini,l[j]-l[i])
    i+=1 
    j+=1 
print(mini)
