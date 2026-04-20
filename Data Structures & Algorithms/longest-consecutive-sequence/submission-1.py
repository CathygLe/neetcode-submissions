class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        result = 0 

        for num in nums:
            if (num+1) in nums:
                longest += 1

                while (num+1) in nums:
                    num = num + 1
                    longest += 1
                    result = max(longest, result)
            longest = 0

        return result 

        

