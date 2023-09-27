  #include<bits/stdc++.h>
  using namespace std;
  bool isValid(string s)
    {
    
        stack<char>st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                st.push(s[i]);
            }
            else
            {
                if(st.empty())
                {
                    return 0;
                }
                if(s[i]==')' && st.top()!='('){return 0;}
                if(s[i]=='}' && st.top()!='{'){return 0;}
                if(s[i]==']' && st.top()!='['){return 0;}
                st.pop();
                
            }
       }
        return st.empty();
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        if(isValid(s))
        {
            cout<<"True"<<endl;
        }
        else{
            cout<<"False"<<endl;
        }
    }
}
