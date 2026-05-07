class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for i in range(len(nums)):
            heapq.heappush(self.nums, nums[i])
            if i >= k:
                heapq.heappop(self.nums)
                
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]