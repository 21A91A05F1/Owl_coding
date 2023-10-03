#include<bits/stdc++.h>
using namespace std;
int main()
{
    int r1,c1;
    cin>>r1>>c1;
    int num1[r1][c1];
    for(int i=0;i<r1;i++)
    {
        for(int j=0;j<c1;j++)
        {
            cin>>num1[i][j];
        }
    }
    int r2,c2;
    cin>>r2>>c2;
    int num2[r2][c2];
    for(int i=0;i<r1;i++)
    {
        for(int j=0;j<c1;j++)
        {
            cin>>num2[i][j];
        }
    }
    int mul[r1][c2];
    for(int i=0;i<r1;i++)
    {
        for(int j=0;j<c2;j++)
        {
            mul[i][j]=0;
            for(int k=0;k<r2;k++)
            {
                mul[i][j]+=num1[i][k]*num2[k][j];
            }
        }
    }
    for(int i=0;i<r1;i++)
    {
        for(int j=0;j<c2;j++)
        {
            if(j==c2-1)
            {
                cout<<mul[i][j];
            }
            else  cout<<mul[i][j]<<" ";
        }
        cout<<endl;
    }
}
'''
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
'''
