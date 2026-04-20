class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key = num, val = index 


        for i in range(len(nums)):
            result = target - nums[i]

            if result in seen:
                return [seen[result], i]
            else: 
                seen[nums[i]] = i 
            
        