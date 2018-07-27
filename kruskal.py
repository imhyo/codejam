from graph import Graph
from union_find import UnionFind


# Kruskal's minimum spanning tree algorithm
def kruskal(graph):
    ret = 0
    result = []
    edges = []
    for u in graph:
        for v, c in graph[u]:
            edges.append((u, v, c))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(len(graph.V))

    for u, v, c in edges:
        if uf.find(u) == uf.find(v):
            continue
        uf.union(u, v)
        result.append((u, v))
        ret += c

    return ret, result
