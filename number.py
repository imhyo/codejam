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
