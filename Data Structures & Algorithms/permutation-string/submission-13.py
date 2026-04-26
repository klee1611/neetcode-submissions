class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        count = [0] * 26
        for c in s1:
            count[ord(c) - ord('a')] += 1

        l, r = 0, 0
        while r < len_s1:
            count[ord(s2[r]) - ord('a')] -= 1
            r += 1

        while r < len_s2:
            print(l, r, count)
            res = True
            for i in range(26):
                if count[i] != 0:
                    res = False
            if res:
                return True

            count[ord(s2[l]) - ord('a')] += 1
            count[ord(s2[r]) - ord('a')] -= 1
            l, r = l + 1, r + 1

        res = True
        for i in range(26):
            if count[i] != 0:
                res = False
        return res