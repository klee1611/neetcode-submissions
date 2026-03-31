class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1, count_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        i, j = 0, len(s1)-1
        while j < len(s2):
            if tuple(count_s1) == tuple(count_s2):
                return True
            count_s2[ord(s2[i]) - ord('a')] -= 1
            i, j = i+1, j+1
            if j < len(s2):
                count_s2[ord(s2[j]) - ord('a')] += 1

        return False