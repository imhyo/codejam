class BellmanFord:
    def __init__(self, N, graph):
        self.N = N
        self.graph = graph

    def run(self, src):
        dist = [int(1e9) for _ in range(self.N + 1)]
        dist[src] = 0
        updated = True
        count = 0
        while updated:
            count += 1
            if count > self.N:
                return None
            updated = False
            for here in self.graph:
                if here == int(1e9):
                    continue
                for there, c in self.graph[here]:
                    if dist[here] + c < dist[there]:
                        updated = True
                        dist[there] = dist[here] + c
        return dist
