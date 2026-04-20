class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # convert into max heap (therefore, must turn negative)
        # max_heap = [-s for s in nums]
        # heapq.heapify(max_heap)

        # # find the kth "smallest" element (aka biggest negative)
        # while k > 0:
        #     val = heapq.heappop(max_heap)

        #     # decrement
        #     k -= 1
        
        # # return it's true value since we initially turned them all negative
        # return -1*val


        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)

            # if len is greater than k, pop the smallest number
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # once array is iterated through, only k largest will remain in heap 
        return minHeap[0]
        