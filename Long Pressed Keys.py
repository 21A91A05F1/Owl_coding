n=input()
s=input()
# print(n,s)
j=0
for i in n:
    f=0
    while(j<len(s) and s[j]==i):
        j+=1
        f=1
    if(f==0):pa
        print('false')
        quit(0)
if(j<len(s)):
    print('false')
else:
    print('true')

'''
Long Pressed Keys
Program Description :
Your friend is typing his name into a keyboard, sometimes when typing a character the key might get pressed long and the character will be typed 1 or more times..

you will be given two strings original string and typed string. you need to examine the strings and print true if it was origina string with some characters being long pressed else print false.
 

Input Format :
The first line contains an original string.

the second line contains a typed string.

Output Format :
Print "true" of "false" based on problem description.

Input :
sekhar

sssekharrrrr


Output :
true


Constraints :
1< len(original), len(typed) <=10^5
'''
