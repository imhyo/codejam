from heapq import heappush, heappop


def dijkstra(graph, src):
    N = len(graph)
    dist = {graph.V[x]: -1 for x in range(N)}
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        cost, u = heappop(pq)
        if 0 <= dist[u] < cost or not graph[u]:
            continue

        for v, c in graph[u]:
            next_dist = cost + c
            if dist[v] == -1 or dist[v] > next_dist:
                dist[v] = next_dist
                heappush(pq, (next_dist, v))
    return dist
