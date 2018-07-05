def bellman_ford(graph, src):
    dist = {}
    for v in graph.V:
        dist[v] = int(1e9)
    dist[src] = 0
    updated = True
    count = 0
    while updated:
        count += 1
        if count > len(graph):
            return None
        updated = False
        for u in graph:
            if dist[u] == int(1e9):
                continue
            for v, c in graph[u]:
                if dist[u] + c < dist[v]:
                    updated = True
                    dist[v] = dist[u] + c
    return dist
