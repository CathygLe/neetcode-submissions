class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        if not numSet:
            return 0
        result = 1
        
        for num in numSet:
            if not num - 1 in numSet:
                length = 1

                while num + 1 in numSet:
                    length += 1
                    num += 1

                    result = max(length, result)
        return result 

