#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    int k;
    cin>>k;
   int mini=INT_MAX;
    for(int i=0;i<n;i++)
    {
        int s=0;
        for(int j=i;j<n;j++)
        {
            s+=arr[j];
            if(s>=k)
            {
                mini=min(mini,j-i+1);
            }
        }
    }
    if(mini==INT_MAX)cout<<0<<endl;
    else cout<<mini<<endl; 
}
