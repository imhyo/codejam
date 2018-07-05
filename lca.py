# Lowest Common Ancestor
class LCA:
    def __init__(self, graph):
        self.graph = graph
        self.depth = {graph.V[x]: 0 for x in range(0, len(graph))}
        self.ancestor = {graph.V[x]: [] for x in range(0, len(graph))}
        self.dfs()

    def get_ancestor(self, u, p):
        self.ancestor[u].append(p)
        i = 1
        while self.depth[u] - 2**i >= 0:
            temp = self.ancestor[u][i - 1]
            self.ancestor[u].append(self.ancestor[temp][i - 1])
            i += 1

    def dfs(self):
        self.depth[None] = -1
        stack = [(1, None)]
        while stack:
            u, p = stack.pop()
            self.depth[u] = self.depth[p] + 1
            self.get_ancestor(u, p)
            if u in self.graph:
                for v in self.graph[u]:
                    if v != p:
                        stack.append((v, u))

    def get(self, u, v):
        if self.depth[u] != self.depth[v]:
            if self.depth[u] > self.depth[v]:
                u, v = v, u
            for i in range(len(self.ancestor[v]) - 1, -1, -1):
                if self.depth[u] <= self.depth[v] - 2**i:
                    v = self.ancestor[v][i]

        ans = u
        if u != v:
            for i in range(len(self.ancestor[u]) - 1, -1, -1):
                if self.depth[u] - 2**i >= 0:
                    if self.ancestor[u][i] != self.ancestor[v][i]:
                        u = self.ancestor[u][i]
                        v = self.ancestor[v][i]
                    else:
                        ans = self.ancestor[u][i]
        return ans
