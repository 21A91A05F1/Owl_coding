#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    map<int,int>mpp;
    vector<int>ve;
    for(int i=0;i<n;i++)
    {
        int k;
        cin>>k;
        ve.push_back(k);
        mpp[ve[i]]++;
    }
    int s=0;
    for(auto it:mpp)
    {
        s+=(it.second)/2;
    }
    cout<<s;
}
