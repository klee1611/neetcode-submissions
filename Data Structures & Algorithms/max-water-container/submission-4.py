class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h_l, h_r = heights[l], heights[r]
            res = max(res, min(h_l, h_r) * (r - l))

            if h_l < h_r:
                l += 1
            else:
                r -= 1

        return res