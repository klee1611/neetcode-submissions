class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        s1 = "".join(l1)
        s2 = "".join(l2)
        if s1 == s2:
            return True
        return False