
m1,m2=map(int,input().split())
mat1=[list(map(int,input().split()))for i in range(m2)]
n1,n2=map(int,input().split())
mat2=[list(map(int,input().split()))for i in range(n2)]
res=[[0 for x in range(n2)]for y in range(m1)]
for i in range(m1):
    for j in range(n2):
        res[i][j]=0
        for k in range(m2):
            res[i][j]+=mat1[i][k]*mat2[k][j]
for i in range(m1):
    for j in range(n2):
        if j!=n2-1:
            print(res[i][j],end=' ')
        else:
            print(res[i][j],end='')
    print()
