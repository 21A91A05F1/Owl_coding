#include<bits/stdc++.h>
using namespace std;
int isfact(int n)
{
    int d=0;
    for(int  i = 1  ; i<=sqrt(n) ; i++)
    {
        if(n%i==0 and i!=sqrt(n)) d+=2;
        if(n%i==0 and i==sqrt(n)) d++;
    }
    if(d==4) return 1;
    return 0;
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m,c=0;
        cin>>n>>m;
        for(int  i = n ; i <=m ;i++)
        {
            if(isfact(i))
            {
                c++;
            }
        }
        cout<<c<<endl;
    }
}
