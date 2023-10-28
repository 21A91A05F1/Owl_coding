x1,v1,x2,v2=map(int,input().split())
if(x1==x2 or v1==v2):
    print("YES")
elif(v1==v2 and x1!=x2):
    print("NO")
elif((x2-x1)%(v1-v2)==0 and (x2-x1)//(v1-v2)>=0):
    print("YES")
else:
    print("NO")
