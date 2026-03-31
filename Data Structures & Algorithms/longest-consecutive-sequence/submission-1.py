class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        
        length = 1
        max_length = 1
        prev = heapq.heappop(nums)
        for i in range(len(nums)):
            current = heapq.heappop(nums)
            if current == prev:
                continue
            print(prev)
            if current == prev + 1:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 1
            prev = current
            print(current, length)

        if length > max_length:
            return length
        
        return max_length