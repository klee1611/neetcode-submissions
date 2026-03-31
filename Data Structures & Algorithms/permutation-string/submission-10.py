class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        l, r = 0, len(s1)-1
        while r < len(s2):
            res = True
            for i in range(26):
                if s1_count[i] != s2_count[i]:
                    res = False
                    break
            if res == True:
                return True

            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                s2_count[ord(s2[r]) - ord('a')] += 1

        return False