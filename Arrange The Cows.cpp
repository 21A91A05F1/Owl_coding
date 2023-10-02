#include<bits/stdc++.h>
using namespace std;
bool can_we_place(int arr[],int dist,int k,int n)
{
    int c=1,last=arr[0];
    for(int i=1;i<n;i++)
    {
        if(arr[i]-last>=dist) 
        {
            c++;
            last=arr[i];
        }
        if(c>=k) return true;
    }
    
    return false;
}
int main()
{
    int n,k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    sort(arr,arr+n);
    int low=1,high=arr[n-1]-arr[0];
    while(low<=high)
    {
        int mid=(low+high)/2;
        if(can_we_place(arr,mid,k,n)==true) 
        {
            low=mid+1;
        }
        else
        {
            high=mid-1;
        }
    }
    cout<<high;
}
