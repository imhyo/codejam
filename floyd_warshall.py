def floyd_warshall(N, edge):
    dist = [[int(1e9) for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
    for u in edge:
        for v, c in edge[u]:
            dist[u][v] = c
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if dist[i][k] == int(1e9):
                continue
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
