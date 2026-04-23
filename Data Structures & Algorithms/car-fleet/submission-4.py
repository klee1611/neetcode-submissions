class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            cars.append([p, (target - p) / s])

        cars.sort(key = lambda car: car[0], reverse = True)

        fleets = []
        for p, t in cars:
            if not fleets:
                fleets.append(t)
                continue
            if t > fleets[-1]:
                fleets.append(t)

        return len(fleets)