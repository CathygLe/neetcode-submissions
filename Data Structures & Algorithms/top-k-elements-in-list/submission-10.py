class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        

        heapped = []

        for item in counts:
            heapq.heappush(heapped, [counts[item], item])
            
        while len(heapped) > k:
            heapq.heappop(heapped)
        
        result = []
        while heapped:
            count, val = heapq.heappop(heapped)
            result.append(val)      
        return result  