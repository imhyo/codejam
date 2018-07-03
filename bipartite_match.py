from collections import deque


# Hopcroft Karp's Bipartite Match Algorihm
# This code is based on pseudo code of Wikipedia.
# Time complexity is sqrt(V) * E where V is # of nodes and E is # of edges.
class BipartiteMatch:
    def __init__(self, U, V, adj):
        self.U = U
        self.V = V
        self.adj = adj
        self.pair_u = [-1 for _ in range(U)]
        self.pair_v = [-1 for _ in range(V)]
        self.dist = [0 for _ in range(U + 1)]

    def bfs(self):
        q = deque()
        for u in range(self.U):
            if self.pair_u[u] == -1:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = int(1e9)
        self.dist[self.U] = int(1e9)
        while q:
            u = q.popleft()
            if self.dist[u] < self.dist[self.U]:
                for v in range(self.V):
                    if self.adj[u][v]:
                        if self.dist[self.pair_v[v]] == int(1e9):
                            self.dist[self.pair_v[v]] = self.dist[u] + 1
                            q.append(self.pair_v[v])
        return self.dist[self.U] != int(1e9)

    def dfs(self, u):
        if u != -1:
            for v in range(self.V):
                if self.adj[u][v]:
                    if self.dist[self.pair_v[v]] == self.dist[u] + 1:
                        if self.dfs(self.pair_v[v]):
                            self.pair_v[v] = u
                            self.pair_u[u] = v
                            return True
            self.dist[u] = int(1e9)
            return False
        return True

    def match(self):
        size = 0
        while self.bfs():
            for u in range(self.U):
                if self.pair_u[u] == -1:
                    if self.dfs(u):
                        size += 1
        return size
