class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [] 
        nums.sort()

        def dfs(i, rsf):

            if i >= len(nums):
                res.append(rsf.copy())
                return

            rsf.append(nums[i])
            dfs(i + 1, rsf)

            rsf.pop()

            while i + 1 < len(nums) and nums[i] ==  nums[i+1]:
                i += 1
            
            dfs(i + 1, rsf)

            
        dfs(0, [])

        return res
        