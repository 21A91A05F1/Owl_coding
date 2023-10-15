#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int s=0;
    int temp=n;
    while(n!=0)
    {
        s+=n%10;
        n/=10;
    }
    if(temp%s==0) cout<<"True";
    else cout<<"False";
}
