class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True, key = lambda c: c[0])

        stack = []
        for car in cars:
            t = (target - car[0]) / car[1]
            if stack and stack[-1] >= t:
                continue
            stack.append(t)

        return len(stack)