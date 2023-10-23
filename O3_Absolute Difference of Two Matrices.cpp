#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int num1[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>num1[i][j];
        }
    }
    int num2[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>num2[i][j];
        }
    }
    int sub[n][n];
     for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            sub[i][j]=abs(num1[i][j]-num2[i][j]);
        }
    }
      for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(j==n-1) cout<<sub[i][j];
            else cout<<sub[i][j]<<" ";
        }
        cout<<endl;
    }
}
