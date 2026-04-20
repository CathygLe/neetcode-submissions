class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1

        
        heap = []

        for num, repeats in count.items():
            heapq.heappush(heap, (repeats, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            val = heapq.heappop(heap) 
            res.append(val[1])


        return res




        