class CountSquares:

    def __init__(self):
        self.x_idx = collections.defaultdict(list)
        self.y_idx = collections.defaultdict(list)
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_idx[x].append(y)
        self.y_idx[y].append(x)
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for y1 in self.x_idx[x]:
            if y1 == y:
                continue
            for x1 in self.y_idx[y1]:
                if x1 == x:
                    continue
                #print(x1, y, self.points[(x1, y)])
                count += self.points[(x1, y)]
        return count