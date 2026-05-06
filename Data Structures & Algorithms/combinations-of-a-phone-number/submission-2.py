class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = [""]
        patterns = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        for d in digits:
            new_res = []
            for p in patterns[d]:
                for r in res:
                    new_res.append(r + p)
            res = new_res

        return res
