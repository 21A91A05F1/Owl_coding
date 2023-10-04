#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    vector<int>ve1;
    for(int i=0;i<n;i++) 
    {
        cin>>arr[i];
        ve1.push_back(arr[i]);
    }
    vector<int>ve2;
    for(int i=0;i<n;i++ )
    {
        int maxi=-1;
        for(int j=0;j<i;j++)
        {
            if(ve1[j]<ve1[i])
            {
                maxi=max(maxi,arr[j]);
            }
        }
        ve2.push_back(maxi);
    }
    for(auto it:ve2) cout<<it<<" ";
}
