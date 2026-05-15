class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [] 
        nums.sort()

        if not nums:
            return []

        def dfs(i, rsf):
            if i >= len(nums):
                if rsf in res:
                    return
                else:
                    res.append(rsf.copy())
                    return

            rsf.append(nums[i])
            dfs(i+1, rsf)


            rsf.pop()

            dfs(i+1, rsf)        
        
        dfs(0, [])

        return res