def reachable(graph, src, dst):
    visited = {}
    for v in graph.V:
        visited[v] = False
    stack = [src]
    visited[src] = True
    while stack:
        u = stack.pop()
        if u in graph:
            for v in graph[u]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True
                    if v == dst:
                        return True
    return False
