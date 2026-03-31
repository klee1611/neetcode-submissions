class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1

        heap = [-c for c in counts.values()]
        cool_q = deque()
        time = 1
        while heap or cool_q:
            if cool_q and cool_q[0][1] == time:
                c, t = cool_q.popleft()
                heapq.heappush(heap, c)
            if heap:
                c = heapq.heappop(heap)
                c += 1
                if c < 0:
                    cool_q.append((c, time+n+1))
            time += 1
            print(heap, cool_q)

        return time-1