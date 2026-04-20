class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums: 
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        maxHeap = []

        for num, count in counts.items():
            heapq.heappush(maxHeap, [count,num])

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        result = []
        while (maxHeap):
            count, num = heapq.heappop(maxHeap)
            result.append(num)

        return result
            
            
        