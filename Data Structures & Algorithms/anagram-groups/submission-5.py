class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = defaultdict(list)

        for s in strs:
            sorted_hash["".join(sorted(s))].append(s)

        return [ v for v in sorted_hash.values() ]