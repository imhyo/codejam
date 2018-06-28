# String submatching
# find N from H
# the function 'search' returns the list of matched index

class KMP:
    def __init__(self, H, N):
        self.H = H
        self.N = N
        self.submatch = [0 for _ in range(len(N))]

    def get_submatch(self):
        begin = 1
        matched = 0
        while begin + matched < len(self.N):
            if self.N[begin + matched] == self.N[matched]:
                matched += 1
                self.submatch[begin + matched - 1] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - self.submatch[matched - 1]
                    matched = self.submatch[matched - 1]

    def search(self):
        self.get_submatch()
        ans = []
        begin, matched = 0, 0
        while begin <= len(self.H) - len(self.N):
            if matched < len(self.N) and self.H[begin + matched] == self.N[matched]:
                matched += 1
                if matched == len(self.N):
                    ans.append(begin)
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - self.submatch[matched - 1]
                    matched = self.submatch[matched - 1]
        return ans
