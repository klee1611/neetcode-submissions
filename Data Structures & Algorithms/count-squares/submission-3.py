class CountSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for pt, c in self.points.items():
            x1, y1 = pt
            if x1 == x or y1 == y:
                continue
            if abs(x1 - x) != abs(y1 - y):
                continue
            count += self.points.get((x1, y), 0) * self.points.get((x, y1), 0) * c
        return count