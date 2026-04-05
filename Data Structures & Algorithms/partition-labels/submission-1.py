class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n < 2:
            return [1]

        freq = defaultdict(list)
        for i in range(n):
            freq[s[i]].append(i)

        res = []
        l, r = 0, 0
        while r < n:
            next_r = freq[s[r]][-1]
            for i in range(l, r):
                next_r = max(next_r, freq[s[i]][-1])
            if next_r == r:
                res.append(r - l + 1)
                l = r + 1
                r = r + 1
            else:
                r = next_r
            print(res)

        return res