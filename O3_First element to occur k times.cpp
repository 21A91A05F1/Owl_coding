#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    int k;
    map<int,int>mpp;
    vector<pair<int,int>>pq;
    for(int i=0;i<n;i++) 
    {
        cin>>arr[i];
    }
    cin>>k;
    int res=-1;
    for(int i=0;i<n;i++) 
    {
        mpp[arr[i]]++;
        if(mpp[arr[i]]==k) 
        {
            res=arr[i];
            break;
        }
    }
    cout<<res;
} 
