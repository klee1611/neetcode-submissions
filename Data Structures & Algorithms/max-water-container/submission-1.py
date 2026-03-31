class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_v = 0
        while i < j:
            if heights[i] <= heights[j]:
                cur_v = heights[i] * (j-i)
                if cur_v > max_v:
                    max_v = cur_v
                i += 1
            else:
                cur_v = heights[j] * (j-i)
                if cur_v > max_v:
                    max_v = cur_v
                j -=1
        return max_v