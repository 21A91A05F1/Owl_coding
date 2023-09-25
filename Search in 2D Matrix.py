n,m=map(int,input().split())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
k=int(input())
c=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]==k):
            c+=1
            print("true")
            break 
    if(c):
        break
else:
    print("false")
