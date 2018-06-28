from heapq import heappop, heappush


class Dijkstra:
    def __init__(self, N, graph):
        self.N = N
        self.graph = graph

    def run(self, src):
        dist = [-1 for _ in range(self.N + 1)]
        dist[src] = 0
        pq = []
        heappush(pq, (0, src))
        while len(pq) > 0:
            cost, here = heappop(pq)

            if 0 <= dist[here] < cost or here not in self.graph:
                continue

            for there, c in self.graph[here]:
                next_dist = cost + c
                if dist[there] == -1 or dist[there] > next_dist:
                    dist[there] = next_dist
                    heappush(pq, (next_dist, there))
        return dist


