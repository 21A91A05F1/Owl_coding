s=input().split()
s.sort(key=lambda word:(len(word),word))
print(*s)
