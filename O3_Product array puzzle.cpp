#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    int p=1,z=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]!=0) p*=arr[i];
        else z++;
    }
    vector<int>res;
    for(int i=0;i<n;i++)
    {
        if(z==1)
        {
            if(arr[i]==0) res.push_back(p);
            else res.push_back(0);
        }
        else if(z>1)
        {
            res.push_back(0);
        }
        else
        {
            res.push_back(p/arr[i]);
        }
    }
    for(auto it:res) cout<<it<<" ";
}
