#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin,s);
    map<char,int>mpp;
    for(auto it:s)
    {
        mpp[tolower(it)]++;
    }
    string res="";
    for(auto it:mpp)
    {
        if(it.second==1)
        {
           res+=(it.first);
        }
    }
    cout<<res;
}
