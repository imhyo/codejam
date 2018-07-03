from collections import deque


class NetworkFlow:
    def __init__(self, N, capacity):
        self.N = N
        self.capacity = capacity

    def bfs(self, flow, source, sink):
        parent = [-1 for _ in range(self.N)]
        q = deque()
        parent[source] = source
        q.append(source)
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(self.N):
                if self.capacity[u][v] - flow[u][v] > 0 and parent[v] == -1:
                    q.append(v)
                    parent[v] = u
        return parent

    def max_flow(self, source, sink):
        flow = [[0 for _ in range(self.N)] for _ in range(self.N)]
        total_flow = 0
        while True:
            parent = self.bfs(flow, source, sink)
            if parent[sink] == -1:
                break
            amount = int(1e9)
            p = sink
            while p != source:
                amount = min(amount, self.capacity[parent[p]][p] - flow[parent[p]][p])
                p = parent[p]
            p = sink
            while p != source:
                flow[parent[p]][p] += amount
                flow[p][parent[p]] -= amount
                p = parent[p]
            total_flow += amount
        return total_flow
