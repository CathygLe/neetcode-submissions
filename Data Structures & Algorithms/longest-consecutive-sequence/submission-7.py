class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        longest = 1 


        for num in nums:
            count = 1
            while (num + 1) in nums:
                count += 1
                num += 1
                
                longest = max(longest, count)

        return longest 
        

