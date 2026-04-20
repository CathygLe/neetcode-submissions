class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else: 
                counts[num] = 1

        heap = [] 

        for num, count in counts.items():
            heapq.heappush(heap, [count,num])
        

        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        while (heap):
            count, val = heapq.heappop(heap)
            result.append(val)
        return result 