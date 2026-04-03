class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra's algo
        prices = defaultdict(list)
        for s, d, price in flights:
            prices[s].append((d, price))            

        min_heap = [(0, src, -1)] # price, dist, count
        while min_heap:
            price, dist, count = heapq.heappop(min_heap)
            if count > k:
                continue
            if dist == dst:
                return price
            
            count += 1
            if count > k:
                continue
            for dist_next, price_next in prices[dist]:
                heapq.heappush(
                    min_heap, (price + price_next, dist_next, count)
                )

        return -1