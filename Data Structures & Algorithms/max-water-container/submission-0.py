class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                volume.append(min(heights[i], heights[j]) * (j-i))

        return max(volume)