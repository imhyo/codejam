class SegmentTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_value = {}
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

    def query_sum(self, start, end):
        return self._query_sum(start, end, self.start, self.end)

    def query_len(self, start, end):
        return self._query_len(start, end, self.start, self.end)

    def _init(self, start, end):
        self.max_value[(start, end)] = 0
        self.sum_value[(start, end)] = 0
        self.len_value[(start, end)] = 0
        if start < end:
            mid = start + int((end - start) / 2)
            self._init(start, mid)
            self._init(mid+1, end)

    def _add(self, start, end, weight, in_start, in_end):
        key = (in_start, in_end)
        if in_start == in_end:
            self.max_value[key] += weight
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


