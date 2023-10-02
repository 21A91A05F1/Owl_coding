#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    int low=0,high=n-1,f=0;
    while(low<=high)
    {
        int mid=(low+high)/2;
        if(arr[mid]==k)
        {
            f=1;
            cout<<arr[mid]<<" ";
            break;
        }
        else if(arr[mid]<k)
        {
            cout<<arr[mid]<<" ";
            low=mid+1;
        }
        else
        {
            cout<<arr[mid]<<" ";
            high=mid-1;
        }
    }
    if(f==0) cout<<"-1";
    
}
