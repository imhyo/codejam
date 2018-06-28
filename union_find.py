class UnionFind:
    def __init__(self, N):
        self.tree = [i for i in range(N + 1)]

    def find(self, n):
        list = []
        p = self.tree[n]
        while p != n:
            list.append(n)
            n = p
            p = self.tree[n]

        for n in list:
            self.tree[n] = p

        return p

    def union(self, n, m):
        p = self.find(n)
        q = self.find(m)
        self.tree[q] = p
