p = input()
s = 0
num = 0
sign = 1
for c in p:
    if c.isdigit():
        num = num * 10 + int(c)
    elif c == '-':
        sign = -1
    elif p[-1].isdigit():
        s += (sign * num)
        num = 0
        sign = 1
s+=(sign * num)
print(s)
