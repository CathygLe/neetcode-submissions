class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [-s for s in nums]
        heapq.heapify(max_heap)

        while k > 0:
            val = heapq.heappop(max_heap)
            k -= 1
        
        return -1*val
        