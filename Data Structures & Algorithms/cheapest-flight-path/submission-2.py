class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f_hash = defaultdict(list)
        for f_source, f_dist, price in flights:
            f_hash[f_source].append((f_dist, price))
        costs = [float('inf') for i in range(n)]
        costs[src] = 0

        q = deque([(src, 0)])
        for i in range(k+1):
            next_q = deque()
            while q:
                vertex, cost = q.popleft()              

                for f_next, price in f_hash[vertex]:
                    if price + cost < costs[f_next]:
                        costs[f_next] = price + cost
                        next_q.append((f_next, price + cost))
            q = next_q

        return costs[dst] if costs[dst] < float('inf') else -1