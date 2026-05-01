class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = {}

        def tracking(idx_1, idx_2, idx_3):
            if idx_3 == len(s3):
                return idx_1 == len(s1) and idx_2 == len(s2)

            if (idx_1, idx_2) in dp:
                return dp[(idx_1, idx_2)]

            dp[(idx_1, idx_2)] = False
            if idx_1 < len(s1) and s1[idx_1] == s3[idx_3]:
                dp[(idx_1, idx_2)] = tracking(idx_1 + 1, idx_2, idx_3 + 1)

            if not dp[(idx_1, idx_2)] and idx_2 < len(s2) and s2[idx_2] == s3[idx_3]:
                dp[(idx_1, idx_2)] = tracking(idx_1, idx_2 + 1, idx_3 + 1)

            return dp[(idx_1, idx_2)]

        return tracking(0, 0, 0)