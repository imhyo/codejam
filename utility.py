dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def neighbor(N, M, y, x):
    ans = []
    for dy, dx in dd:
        y1, x1 = y + dy, x + dx
        if y1 < 0 or y1 >= N or x1 < 0 or x1 >= M:
            continue
        ans.append((y1, x1))
    return ans


def get_edge(M):
    edge = {}
    for _ in range(M):
        a, b, c = [int(x) for x in input().split()]
        if a not in edge:
            edge[a] = []
        if b not in edge:
            edge[b] = []
        edge[a].append((b, c))
        edge[b].append((a, c))
    return edge


def parametric_search(f, left, right):
    ans = 0
    while left < right:
        middle = (left + right) // 2
        if f(middle):
            ans = max(ans, middle)
            left = middle + 1
        else:
            right = middle

    if f(left):
        ans = max(ans, middle)

    return ans
