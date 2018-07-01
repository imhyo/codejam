from bisect import bisect_right


# Longest Increasing Sub-sequence
def get_lis_size(seq):
    result = [seq[0]]
    for n in seq:
        if n > result[-1]:
            result.append(n)
        else:
            index = bisect_right(result, n)
            if index > 0 and result[index - 1] == n:
                continue
            result[index] = n

    return len(result)


def get_lis(seq):
    lis_size = [1 for _ in range(len(seq))]
    prev = [-1 for _ in range(len(seq))]

    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:
                lis_size[i] = max(lis_size[i], lis_size[j] + 1)
                prev[i] = j

    max_lis_size = 0
    index = -1
    for i in range(len(seq)):
        if lis_size[i] > max_lis_size:
            max_lis_size = lis_size[i]
            index = i

    result = []
    while index >= 0:
        result.append(seq[index])
        index = prev[index]
    return list(reversed(result))
