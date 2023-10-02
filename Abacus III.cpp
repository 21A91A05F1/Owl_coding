#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int arr[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++){
            cin>>arr[i][j];
        }
    }
    int d=0;
    for(int i=0;i<m;i++)
    {
        d=0;
        for(int j=0;j<n;j++)
        {
            if(j==0)
            {
                if(arr[j][i]==1)
                {
                    d+=5;
                }
            }
            else
            {
                if(arr[j][i]==1)
                {
                    d+=1;
                }
            }
        }
        cout<<d;
    }
}
