class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max([interval[0] for interval in intervals])

        timeline = [-1] * (max_start + 1)
        for start, end in intervals:
            timeline[start] = max(timeline[start], end)

        res = []
        start, end = -1, -1
        for i in range(len(timeline)):
            if start == -1 and timeline[i] != -1:
                start = i
            if timeline[i] != -1:
                end = max(end, timeline[i])
            if end == i:
                res.append([start, end])
                start, end = -1, -1

        if start != -1:
            res.append([start, end])
        return res 