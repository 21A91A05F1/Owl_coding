#include<bits/stdc++.h>
using namespace std;
int fun(int n,int a)
{
    if(n==0) return 1;
    int c=0;
    for(int i=a;i<5;i++)
    {
        c+=fun(n-1,i);
    }
    return c;
}
int main()
{
    int n;
    cin>>n;
    cout<<fun(n,0);
}
//cout<<(n+1)*(N+2)*(N+3)*(N+4)//24
