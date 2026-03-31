class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        i, j = 0, len(heights) - 1
        while i < j:
            cur_v = 0
            if heights[i] < heights[j]:
                cur_v = heights[i] * (j-i)
                i += 1
            else:
                cur_v = heights[j] * (j-i)
                j -= 1
            volume = max(volume, cur_v)
        return volume