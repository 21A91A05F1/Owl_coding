/*
Maximum Profit Events
Program Description :
Given a list events of n intervals, the ith element [s, e, p] denotes the starting point s, ending point e, and the profit p earned by choosing the ith event. Find the maximum profit one can achieve by choosing a subset of non-overlapping events.

Two events [s1, e1, p1] and [s2, e2, p2] are said to be non-overlapping if [e1 <= s2] and [s1 < s2]. 

Input Format :
First line denotes a single integer n representing the number of events.

The n subsequent lines contains three space separated integers s, e, p of an event respectively.

Output Format :
A single integer representing the maximum profit earned by choosing a subset of events.

Input :
3

1 2 4

1 5 7

2 4 4


Output :
8

Explanation:

By choosing the events [1, 2, 4] and [2, 4, 4], we can get a maximum profit of 8 as they are non-overlapping.


Constraints :
1 <= n <= 10^5

1 <= s < e <= 10^5

1 <= p <= 10^5
*/
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
