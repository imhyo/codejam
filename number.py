from math import sqrt


def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def lcd(a, b):
    return a * b // gcd(a, b)


def factor(n):
    ans = set([])
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    return ans


def get_prime(N):
    prime = [True for _ in range(N + 1)]
    prime[0] = False
    prime[1] = False
    for n in range(2, int(sqrt(N)) + 1):
        if prime[n]:
            for k in range(n*2, N + 1, n):
                prime[k] = False
    return {n for n in range(2, N + 1) if prime[n]}


def factorize(prime, n):
    ans = {}
    for p in prime:
        while n % p == 0:
            if p not in ans:
                ans[p] = 0
            ans[p] += 1
            n //= p
            if n == 1:
                return ans
