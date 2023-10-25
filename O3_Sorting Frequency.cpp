/*
Input :
8

6 6 4 7 5 4 4 3 


Output :
4 6 3 5 7 


Constraints :
1 ≤ n ≤ 1000

-1000 ≤ arr[i] ≤ 1000
*/
#include<bits/stdc++.h>
using namespace std;
bool comp(pair<int,int>&a , pair<int,int>&b)
{
    if(a.second==b.second) return a.first<b.first;
    return a.second>b.second;
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    map<int,int>mpp;
    vector<pair<int,int>>pq;
    for(int i=0;i<n;i++) 
    {
        cin>>arr[i];
        mpp[arr[i]]++;
    }
    for(auto it:mpp)
    {
        pq.push_back({it.first,it.second});
    }
    sort(pq.begin(),pq.end(),comp);
    for(auto it:pq)
    {
        cout<<it.first<<" ";
    }
}
