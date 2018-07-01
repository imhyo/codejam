from collections import deque


def topological_sort(N, edge):
    in_degree = [0 for _ in range(N + 1)]
    for u in edge:
        for v in edge[u]:
            in_degree[v] += 1
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        u = queue.pop()
        result.append(u)
        if u in edge:
            for v in edge[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    if len(result) != N:
        return []
    else:
        return result
