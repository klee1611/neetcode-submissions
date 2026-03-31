class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            count["".join(sorted(s))].append(s)

        return [ v for v in count.values() ]