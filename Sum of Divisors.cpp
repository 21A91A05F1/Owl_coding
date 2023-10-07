#include<bits/stdc++.h>
using namespace std;
int fun(int n)
{
    long long  s=0;
    for(int i=1;i<=sqrt(n);i++)
    {
        if(n%i==0)
        {
            if(i==(n/i))
            {
                s+=i;
            }
            else
            {
                s+=i;
                s+=(n/i);
            }
            
        }
    }
    return s;
}
int main()
{
    long long  n;
    cin>>n;
    long long  ans=0;
    for(int i=1;i<=n;i++)
    {
        ans+=fun(i);
    }
    cout<<ans;
}
