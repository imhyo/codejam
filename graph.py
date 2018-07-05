class Graph:
    def __init__(self, V):
        self.V = V
        self.E = {}

    def __setitem__(self, key, value):
        if key not in self.E:
            self.E[key] = []
        self.E[key].append(value)

    def __getitem__(self, item):
        if item not in self.E:
            return []
        else:
            return self.E[item]

    def __len__(self):
        return len(self.V)

    def __repr__(self):
        return repr(self.E)

    def __contains__(self, item):
        return item in self.E

    def __iter__(self):
        return iter(self.E)
