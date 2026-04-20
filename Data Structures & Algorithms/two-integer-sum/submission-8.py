class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            check = target - nums[i] 
            if check in visited:
                return [visited[check], i] 
            
            visited[nums[i]] = i 

        return []


       
    


        