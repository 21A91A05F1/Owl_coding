#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s,res;
    cin>>s;
    stack<char>st;
    int i=0;
    while(i<s.size())
    {
        if(s[i]==')')
        {
            string temp;
           while(!st.empty() and i<s.size() and st.top()=='(' and s[i]==')')
           {
                auto t=st.top();
                st.pop();
                if(!st.empty())
                {
                    temp=t+temp;
                    temp+=s[i];
                }
                i++;
           }
           res+=temp;
        }
        else st.push(s[i++]);
    }
    cout<<res<<endl;
}
/*
LEVEL-2/HARD/POINTS: 80
Codemind Parentheses
Program Description :
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

print s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Input Format :
The program should accept a single input string s, which is a valid parentheses string.

Output Format :
The program should return a string with the outermost parentheses removed from every primitive valid parentheses string in the primitive decomposition of s.

Input :
(()())(()) 


Output :
()()() 


Constraints :
1 <= s.length <= 105

s[i] is either '(' or ')'.

s is a valid parentheses string.
*/
