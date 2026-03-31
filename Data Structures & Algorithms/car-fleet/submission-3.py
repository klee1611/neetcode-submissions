class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = []
        for p, s in cars:
            t = (target - p) / s
            if not fleets:
                fleets.append(t)
            elif t > fleets[-1]:
                fleets.append(t)

        return len(fleets)
