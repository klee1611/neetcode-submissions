"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if not n:
            return 0
        if n < 2:
            return 1

        intervals.sort(key = lambda intv: intv.start)
        rooms_heap = []
        for intv in intervals:
            if rooms_heap and rooms_heap[0] <= intv.start:
                heapq.heappop(rooms_heap)
            heapq.heappush(rooms_heap, intv.end)

        return len(rooms_heap)