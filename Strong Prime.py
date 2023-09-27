def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def previous_prime(n):
    while True:
        n -= 1
        if is_prime(n):
            return n

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def strong_prime(n):
    prime1 = previous_prime(n)
    prime2 = next_prime(n)
    mean = (prime1 + prime2) / 2
    return n > mean
N = int(input())
if strong_prime(N):
    print("YES")
else:
    print("NO")
