s=input().split(" ")
k=""
for i in s:
    k+=i
print(min(k),k.count(min(k)),max(k),k.count(max(k)))
