def get_max_box(histogram):
    ans = 0
    stack = [(-1, 0)]
    histogram += [0]
    for i in range(len(histogram)):
        h = histogram[i]
        last_pos = i
        while stack and h <= stack[-1][1]:
            ans = max(ans, stack[-1][1] * (i - stack[-1][0]))
            last_pos = stack[-1][0]
            stack.pop()
        stack.append((last_pos, h))
    return ans
