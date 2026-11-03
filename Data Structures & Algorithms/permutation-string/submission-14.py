class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        counts = [0] * 26
        for c in s1:
            counts[ord(c) - ord('a')] += 1

        l = 0
        counts2 = [0] * 26
        for r in range(n2):
            counts2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == n1:
                if counts == counts2:
                    return True
                counts2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False