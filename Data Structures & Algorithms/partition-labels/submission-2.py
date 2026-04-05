class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = defaultdict(int)
        for i, c in enumerate(s):
            lastIdx[c] = i

        res = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIdx[c])

            if i == end:
                res.append(size)
                size = 0
        return res