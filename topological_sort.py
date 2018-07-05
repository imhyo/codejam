from collections import deque


def topological_sort(graph):
    N = len(graph)
    in_degree = {graph.V[x]: 0 for x in range(N)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    q = deque()
    for v in in_degree:
        if in_degree[v] == 0:
            q.append(v)

    result = []
    while q:
        u = q.pop()
        result.append(u)
        if u in graph:
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
    if len(result) != N:
        return []
    else:
        return result
