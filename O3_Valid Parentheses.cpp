#include<bits/stdc++.h>
using namespace std;
int fun(stack<char>st,string s)
{
     for(int i=0;i<s.size();i++)
    {
       if(s[i]=='(' or s[i]=='{' or s[i]=='[') st.push(s[i]);
       else
       {
            if(st.empty()) 
            {
                return 0;
            }
            if(s[i]==')' and st.top()!='(') return 0;
            if(s[i]=='}' and st.top()!='{') return 0;
            if(s[i]==']' and st.top()!='[') return 0;
            st.pop();
       }
    }
    return st.empty();
}
int main()
{
    string s;
    cin>>s;
    stack<char>st;
    if(fun(st,s)==0) cout<<"False";
    else cout<<"True";
}
