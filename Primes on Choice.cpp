#include<bits/stdc++.h>
using namespace std;
int is_prime(int n)
{
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0) return 0;
    }
    return 1;
}
int main()
{
    int n,r,c;
    cin>>n>>r>>c;
    vector<int>ve;
    if(c==0)
    {
        int k=0;
        for(int i=n-1;i>=0;i--)
        {
            if(is_prime(i)==1)
            {
                k++;
                cout<<i<<" ";
                if(k==r) break;
            }
        }
    }
    else
    {
        int k=0;
        for(int i=n+1;i<=n+1000;i++)
        {
            if(is_prime(i)==1)
            {
                k++;
                cout<<i<<" ";
                if(k==r) break;
            }
        }
    }
}
