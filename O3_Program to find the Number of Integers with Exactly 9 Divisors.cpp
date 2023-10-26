#include<bits/stdc++.h>
using namespace std;
int isdiv(int n)
{
    int d=0;
    for(int  i = 1  ; i <=n ; i++)
    {
        if(n%i==0) d++;
    }
    if(d==9) return 1;
    else return 0;
}
int main()
{
    int n;
    cin>>n;
    vector<int>arr;
    int c=0;
    for(int i = 0 ;  i <=n ; i++)
    {
        if(isdiv(i))
        {
            arr.push_back(i);
            c++;
        }
    }
    for(int  i = 0  ;  i <arr.size() ; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<"Total="<<c;
}
