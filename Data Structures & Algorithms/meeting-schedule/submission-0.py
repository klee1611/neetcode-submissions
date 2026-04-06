"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if 0 == len(intervals):
            return True

        intervals.sort(key = lambda intv: intv.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True