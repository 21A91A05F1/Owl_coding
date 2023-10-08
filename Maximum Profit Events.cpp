#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<vector<int>>arr(n,vector<int>(3,0));
    for(int  i = 0 ;  i< n ;i++)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            cin>>arr[i][j];
        }
    }
    sort(arr.begin(),arr.end());
    vector<int>dp(n,0);
    dp[0]=arr[0][2];
    for(int i = 1 ; i<n ;i++)
    {
        dp[i]=arr[i][2];
        for(int j=i-1 ; j>=0 ;j--)
        {
            if(arr[i][0]>=arr[j][1])
            {
                dp[i]=max(dp[i],dp[j]+arr[i][2]);
            }
        }
    }
    int k=*max_element(dp.begin(),dp.end());
    cout<<k;
}
