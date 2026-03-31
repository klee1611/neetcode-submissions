class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        i,j = 0, len(s)-1
        while i < j:
            print(i, j)
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if i >= j:
                return True
            s_i, s_j = s[i], s[j]
            if s_i.isupper():
                s_i = s_i.lower()
            if s_j.isupper():
                s_j = s_j.lower()
            if s_i != s_j:
                return False
            i += 1
            j -= 1
        return True