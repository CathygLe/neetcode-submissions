class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        if len(nums) == 0:
            result = 0
        else:
            result = 1

        for num in nums:
            if (num+1) in nums:
                longest += 1

                while (num+1) in nums:
                    num = num + 1
                    longest += 1
                    result = max(longest, result)
            longest = 0

        return result 

        

