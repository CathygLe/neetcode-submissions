class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            search = target - nums[i]

            if search in seen:
                return [seen[search], i]
            else: 
                seen[nums[i]] = i
        
            