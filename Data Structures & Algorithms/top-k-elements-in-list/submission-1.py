class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        
        result = []
        for num, repeats in count.items():
            if repeats >= k:
                result.append(num)
        
        return result




        