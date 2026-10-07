class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        if not nums:
            return 0 

        result  = 1 

        for num in numset:
            if  num - 1 not in numset:
                length = 1 
            
                while num + 1 in numset:
                    length += 1
                    num += 1
            
                result = max(result, length)
        return result 



