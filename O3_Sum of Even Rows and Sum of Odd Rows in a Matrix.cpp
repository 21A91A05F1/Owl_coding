#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int s=0;
    int arr[n][m];
    for(int i=0;i<n;i++) 
    {
        for(int j=0;j<m;j++)
        {
            cin>>arr[i][j];
        }
    }
    int s1=0,s2=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
           if(i%2==0) s1+=arr[i][j];
           else s2+=arr[i][j];
        }
    }
    cout<<s1<<" "<<s2;

}
