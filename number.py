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


class Fibonacci:
    def __init__(self, P=0):
        self.m = [[1, 1], [1, 0]]
        self.P = P

    def matmul(self, m1, m2):
        if self.P == 0:
            return [[(m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]), (m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1])],
                 [(m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]), (m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1])]]
        else:
            return [[(m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]) % self.P, (m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]) % self.P],
                 [(m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]) % self.P, (m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]) % self.P]]

    def pow(self, m, n):
        if n == 1:
            return m
        if n % 2 == 1:
            return self.matmul(self.pow(m, n - 1), m)
        else:
            p = self.pow(m, n//2)
            return self.matmul(p, p)

    def get(self, n):
        if n == 0:
            return 0
        m = self.pow(self.m, n)
        return m[1][0]


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
