class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        volume = 0

        while l < r:
            shorter = min(heights[l], heights[r])
            volume = max(volume, (r - l) * shorter)
            if shorter == heights[l]:
                l += 1
            else:
                r -= 1

        return volume