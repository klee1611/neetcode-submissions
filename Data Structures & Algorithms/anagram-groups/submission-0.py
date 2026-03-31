class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for s in strs:
            t = str(sorted(s))
            tmp = "".join(t)
            if tmp in sorted_strs:
                sorted_strs[tmp].append(s)
            else:
                sorted_strs[tmp] = [s]
        return [ v for v in sorted_strs.values()]
