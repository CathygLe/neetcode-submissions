class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1 

        heap = []

        for num, val in count.items():
            heapq.heappush(heap, (val, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            val = heapq.heappop(heap)

            result.append(val[1])

        return result

        