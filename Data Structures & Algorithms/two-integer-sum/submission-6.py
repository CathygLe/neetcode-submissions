class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # num, index

        for i in range(len(nums)): 
            comp = target - nums[i] 

            if comp in visited:
                return [visited[comp], i]
            else:
                visited[nums[i]] = i
        
        