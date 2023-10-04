#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    set<vector<int>>s;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            for(int k=j+1;k<n;k++)
            {
                if(arr[i]+arr[j]+arr[k]==0)
                {
                    vector<int>ve;
                    ve.push_back(arr[i]);
                    ve.push_back(arr[j]);
                    ve.push_back(arr[k]);
                    sort(ve.begin(),ve.end());
                    s.insert(ve);
                }
            }
        }
    }
    cout<<s.size();
}
