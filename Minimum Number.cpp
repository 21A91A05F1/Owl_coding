#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int>ve;
    int s=0;
    for(int i=9;i>=0;i--)
    {
        if(s+i<=n)
        {
            ve.push_back(i);
            s+=i;
        }
    }
    if(s<n) cout<<"-1";
    else
    {
        int res=0;
        for(int i=ve.size()-1;i>=0;i--)
        {
            res=res*10+ve[i];
        }
        cout<<res;
    }
}
