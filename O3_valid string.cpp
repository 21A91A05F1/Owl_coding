#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    map<char,int>mpp;
    for(int i=0;i<s.size();i++)
    {   
        mpp[s[i]]++;
    }
    int a=mpp[s[0]],c=0;
    for(auto it:mpp)
    {
        if(it.second!=a) c+=1;
    }
    if(c<=1) cout<<"Valid String";
    else cout<<"Not Valid";
}
