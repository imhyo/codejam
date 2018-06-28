def reachable(N, edge, src, dst):
    visited = [False for _ in range(N + 1)]
    stack = [src]
    visited[src] = True
    while stack:
        u = stack.pop()
        if u in edge:
            for v in edge[u]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True
                    if v == dst:
                        return True
    return False
