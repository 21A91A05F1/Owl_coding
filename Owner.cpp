#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n],brr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    for(int i=0;i<n;i++) cin>>brr[i];
    int k;
    cin>>k;
    int a=0;
    for(int i=0;i<n;i++)
    {
        if(brr[i]==0) a+=arr[i];
    }
    int l=0,grump=0,maxi=0;
    for(int i=0;i<n;i++)
    {
        if(brr[i]==1)
        {
            grump+=arr[i];
        }
        if((i+1-l)>k)
        {
            if(brr[l]==1) grump-=arr[l];
            l++;
        }
        maxi=max(maxi,grump);   
    }
    cout<<maxi+a;
}
