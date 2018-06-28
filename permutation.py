def unique_permutations_helper(occurences, result, d):
    if d == 0:
        yield result
    else:
        for i in range(4):
            if occurences[i] > 0:
                result.append(i)
                occurences[i] -= 1
                for g in unique_permutations_helper(occurences, result, d - 1):
                    yield g
                occurences[i] += 1
                result.pop()


def unique_permutations(occurences):
    result = []
    d = sum(occurences)
    return unique_permutations_helper(occurences, result, d)


def get_next_permutation(seq):
    length = len(seq)
    for i in range(length - 2, -1, -1):
        if seq[i] < seq[i + 1]:
            break
    else:
        return [-1]

    min_value = length + 1
    min_index = i
    for j in range(i + 1, length):
        if seq[i] < seq[j] < min_value:
            min_value = seq[j]
            min_index = j
    seq[i], seq[min_index] = seq[min_index], seq[i]
    tail = sorted(seq[i + 1:])
    for j in range(i + 1, length):
        seq[j] = tail[j - i - 1]
    return seq


def get_prev_permutation(seq):
    length = len(seq)
    for i in range(length - 2, -1, -1):
        if seq[i] > seq[i + 1]:
            break
    else:
        return [-1]

    max_value = 0
    max_index = i
    for j in range(i + 1, length):
        if max_value < seq[j] < seq[i]:
            max_value = seq[j]
            max_index = j
    seq[i], seq[max_index] = seq[max_index], seq[i]
    tail = sorted(seq[i + 1:], reverse=True)
    for j in range(i + 1, length):
        seq[j] = tail[j - i - 1]
    return seq


