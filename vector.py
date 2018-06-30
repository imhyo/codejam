import math


EPSILON = 1e-7


class Vector:
    def __init__(self, x, y):
        self.x , self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __gt__(self, other):
        return self.x > other.x if self.x != other.x else self.y > other.y

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def norm(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        n = self.norm()
        return Vector(self.x / n, self.y / n)

    def polar(self):
        return math.fmod(math.atan2(self.y, self.x) + 2*math.pi, 2*math.pi)

    def dot(self, other):
        return self.x*other.x + self.y + other.y

    def cross(self, other):
        return self.x*other.y - other.x*self.y

    def project(self, other):
        other = other.normalize()
        return other * other.dot(self)


def triangle_area(a, b, c):
    return abs((b-a).cross(c-a)) / 2


def ccw(p, a, b):   # returns positive if b is counter-clockwise of a
    return (a - p).cross(b - p)


def intersection(a, b, c, d):   # returns intersection of line(a, b) and line(c, d). returns None if they are parallel
    det = (b - a).cross(d - c)
    if (abs(det)) < EPSILON:
        return None
    return a + (b - a)*((c - a).cross(d - c) / det)


def convex_hull(points):
    p0 = min(points)
    index = points.index(p0)
    points[0], points[index] = points[index], points[0]
    points = points[:1] + sorted(points[1:], key=lambda a: (int(1e9) if a.x == p0.x else (a.y - p0.y) / (a.x - p0.x), a.x, a.y))

    hull = []
    for p in points:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull
