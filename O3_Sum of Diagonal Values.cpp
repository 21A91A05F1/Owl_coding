#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int arr[n][m];
    for(int i=0;i<n;i++) 
    {
        for(int j=0;j<m;j++)
        {
            cin>>arr[i][j];
        }
    }
    int s=0;
    for(int i=0;i<min(n,m);i++)
    {
       s+=arr[i][i];
       if(i!=n-i-1)
       {
            s+=arr[n-i-1][i];
       }
    }
    cout<<s;

}
