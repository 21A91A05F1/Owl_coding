s=input()
l=input()
for i in s:
    if l in s:
        print(s.index(l))
        break
else:
    print("-1")
