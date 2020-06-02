class SegmentTree:
    def __init__(self, start, end, data):
        self.start = start
        self.end = end
        self.data = data
        self.max_value = {}
        self.min_value = {}
        self.sum_value = {}
        self.len_value = {}
        self._init(start, end)

    def add(self, start, end, weight=1):
        start = max(start, self.start)
        end = min(end, self.end)
        self._add(start, end, weight, self.start, self.end)
        return True

    def query_max(self, start, end):
        return self._query_max(start, end, self.start, self.end)

    def query_min(self, start, end):
        return self._query_min(start, end, self.start, self.end)

    def query_sum(self, start, end):
        return self._query_sum(start, end, self.start, self.end)

    def query_len(self, start, end):
        return self._query_len(start, end, self.start, self.end)

    def _init(self, start, end):
        if start < end:
            mid = start + int((end - start) / 2)
            max_l, min_l, sum_l, len_l = self._init(start, mid)
            max_r, min_r, sum_r, len_r = self._init(mid + 1, end)
            self.max_value[(start, end)] = max(max_l, max_r)
            self.min_value[(start, end)] = min(min_l, min_r)
            self.sum_value[(start, end)] = sum_l + sum_r
            self.len_value[(start, end)] = len_l + len_r
        else:
            a = self.data[start - self.start]
            self.max_value[(start, end)] = a
            self.min_value[(start, end)] = a
            self.sum_value[(start, end)] = a
            if a == 0:
                self.len_value[(start, end)] = 0
            else:
                self.len_value[(start, end)] = 1

        return self.max_value[(start, end)], self.min_value[(start, end)], self.sum_value[(start, end)], self.len_value[(start, end)]

    def _add(self, start, end, weight, in_start, in_end):
        key = (in_start, in_end)
        if in_start == in_end:
            self.max_value[key] += weight
            self.min_value[key] += weight
            self.sum_value[key] += weight
            self.len_value[key] = 1 if self.sum_value[key] > 0 else 0
            return

        mid = in_start + int((in_end - in_start) / 2)
        if mid >= end:
            self._add(start, end, weight, in_start, mid)
        elif mid+1 <= start:
            self._add(start, end, weight, mid+1, in_end)
        else:
            self._add(start, mid, weight, in_start, mid)
            self._add(mid+1, end, weight, mid+1, in_end)
        self.max_value[key] = max(self.max_value[(in_start, mid)], self.max_value[(mid+1, in_end)])
        self.min_value[key] = min(self.min_value[(in_start, mid)], self.min_value[(mid+1, in_end)])
        self.sum_value[key] = self.sum_value[(in_start, mid)] + self.sum_value[(mid+1, in_end)]
        self.len_value[key] = self.len_value[(in_start, mid)] + self.len_value[(mid+1, in_end)]

    def _query_max(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.max_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_max(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_max(start, end, mid+1, in_end)
            else:
                ans = max(self._query_max(start, mid, in_start, mid),
                        self._query_max(mid+1, end, mid+1, in_end))
        return ans

    def _query_min(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.min_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_min(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_min(start, end, mid+1, in_end)
            else:
                ans = min(self._query_min(start, mid, in_start, mid),
                        self._query_min(mid+1, end, mid+1, in_end))
        return ans

    def _query_sum(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.sum_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_sum(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_sum(start, end, mid+1, in_end)
            else:
                ans = self._query_sum(start, mid, in_start, mid) + self._query_sum(mid+1, end, mid+1, in_end)
        return ans

    def _query_len(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.len_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_len(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_len(start, end, mid+1, in_end)
            else:
                ans = self._query_len(start, mid, in_start, mid) + self._query_len(mid+1, end, mid+1, in_end)

        return ans


# Segment Tree implemented by myself.
class SimpleSegTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.tree = [0 for i in range(4 * (right - left + 1))]
        stack = [(1, left, right)]
        while len(stack) > 0:
            index, left, right = stack.pop()
            self.tree[index] = right - left + 1
            if right > left:
                middle = (left + right) // 2
                stack.append((index * 2, left, middle))
                stack.append((index * 2 + 1, middle + 1, right))

    def query(self, left, right):
        stack = [(1, self.left, self.right)]
        if left > right:
            left, right = right, left
        sum = 0
        while len(stack) > 0:
            index, seg_left, seg_right = stack.pop()
            if left <= seg_left and right >= seg_right:
                sum += self.tree[index]
            elif seg_right < left or seg_left > right:
                continue
            else:
                middle = (seg_left + seg_right) // 2
                stack.append((index * 2, seg_left, middle))
                stack.append((index * 2 + 1, middle + 1, seg_right))
        return sum

    def _add(self, num, d):
        index = 1
        seg_left = self.left
        seg_right = self.right
        while seg_right > seg_left:
            self.tree[index] += d
            middle = (seg_left + seg_right) // 2
            if num <= middle:
                seg_right = middle
                index *= 2
            else:
                seg_left = middle + 1
                index = index * 2 + 1

        self.tree[index] += d

    def delete(self, num):
        self._add(num, -1)

    def add(self, num):
        self._add(num, 1)


from math import ceil, log2


class SegmentTreeWithLazyPropagation:
    def __init__(self, data):
        self.N = len(data)
        h = int(ceil(log2(self.N)))
        self.tree_size = (1 << (h + 1)) - 1
        self.tree = [0 for _ in range(self.tree_size)]
        self.lazy = [0 for _ in range(self.tree_size)]
        self._init(data, 1, 0, self.N - 1)

    def _init(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            self.tree[node] = self._init(data, node*2, start, (start + end)//2) +\
                self._init(data, node*2 + 1, (start + end)//2 + 1, end)
        return self.tree[node]

    def _update_lazy(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1)*self.lazy[node]
            if start != end:
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _update_range(self, node, start, end, left, right, diff):
        self._update_lazy(node, start, end)
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1)*diff
            if start != end:
                self.lazy[node*2] += diff
                self.lazy[node*2 + 1] += diff
            return
        self._update_range(node*2, start, (start + end)//2, left, right, diff)
        self._update_range(node*2 + 1, (start + end)//2 + 1, end, left, right, diff)
        self.tree[node] = self.tree[node*2] + self.tree[node*2 + 1]

    def update_range(self, left, right, diff):
        self._update_range(1, 0, self.N - 1, left, right, diff)

    def _sum(self, node, start, end, left, right):
        self._update_lazy(node, start, end)
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        return self._sum(node*2, start, (start + end)//2, left, right) + \
                    self._sum(node*2 + 1, (start + end)//2 + 1, end, left, right)

    def sum(self, left, right):
        return self._sum(1, 0, self.N - 1, left, right)


# FenwickTree (Binary Indexed Tree) with point update and range query
# the index is 1~N
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0]
        for i in range(1, size+1):
            self.tree.append(i & -i)

    def sum(self, n):
        ans = 0
        while n > 0:
            ans += self.tree[n]
            n &= n-1
        return ans

    def query(self, left, right):
        if left > right:
            left, right = right, left
        return self.sum(right) - self.sum(left-1)

    def _add(self, pos, d):
        while pos <= self.size:
            self.tree[pos] += d
            pos += (pos & -pos)

    def add(self, pos):
        self._add(pos, 1)

    def delete(self, pos):
        self._add(pos, -1)


# FenwickTree (Binary Indexed Tree) with range update and point query
# the index is 0~N-1
class FenwickTreeRangeUpdate:
    def __init__(self, data):
        self.data = data
        self.N = len(data)
        self.ft = [0 for _ in range(self.N + 1)]

    def update(self, p, v):
        p += 1
        while p <= self.N:
            self.ft[p] += v
            p += p & (-p)

    def update_range(self, a, b, v):
        self.update(a, v)
        self.update(b + 1, -v)

    def query(self, a):
        sum = 0
        b = a + 1
        while b > 0:
            sum += self.ft[b]
            b -= b & (-b)
        return sum + self.data[a]
