class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for d in range(n)]
        dist[src] = 0
        for _ in range(k+1):
            next_dist = [ d for d in dist ]
            for s, d, p in flights:
                next_dist[d] = min(next_dist[d], dist[s] + p)
            dist = next_dist

        return -1 if dist[dst] == float('inf') else dist[dst]