// similar to row wise sum of a matrix
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
    int maxi=0;
    for(int i=0;i<n;i++)
    {
        int s=0;
        for(int j=0;j<m;j++)
        {
            s+=arr[i][j];
        }
        maxi=max(maxi,s);
    }
    cout<<maxi;

}
