import math
from math import ceil
t=int(input())
while(t):
    a,b=map(int,input().split())
    print(ceil(a/5)-ceil(b/5))
    t-=1 
