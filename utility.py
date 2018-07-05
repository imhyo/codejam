dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def neighbor(N, M, y, x):
    ans = []
    for dy, dx in dd:
        y1, x1 = y + dy, x + dx
        if y1 < 0 or y1 >= N or x1 < 0 or x1 >= M:
            continue
        ans.append((y1, x1))
    return ans


def parametric_search_max(f, left, right):
    ans = 0
    while left < right:
        middle = (left + right) // 2
        if f(middle):
            ans = max(ans, middle)
            left = middle + 1
        else:
            right = middle

    if f(left):
        ans = max(ans, left)

    return ans


def parametric_search_min(f, left, right):
    ans = int(1e9)
    while left < right:
        middle = (left + right) // 2
        if f(middle):
            ans = min(ans, middle)
            right = middle
        else:
            left = middle + 1

    if f(left):
        ans = min(ans, left)

    return ans
