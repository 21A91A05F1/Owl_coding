#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,k;
    cin>>n>>k;
    int f=0,c=0;
    int p=2;
    vector<int>arr;
    while (n > 1) {
    int p = 2;  
    while (n % p != 0) {
        p++; 
    }
    n = n / p; 
    arr.push_back(p);  
}
    for(auto it:arr)
    {
        //cout<<it<<" ";
        c++;
        if(c==k) 
        {
            cout<<it;
            f=1;
            break;
        }
    }
    if(f==0) cout<<-1<<endl;
}
