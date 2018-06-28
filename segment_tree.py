class SegTree:
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


