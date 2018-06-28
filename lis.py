# Longest Increasing Sequence

def get_lis(seq):
    lis = [1 for _ in range(len(seq))]

    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)
