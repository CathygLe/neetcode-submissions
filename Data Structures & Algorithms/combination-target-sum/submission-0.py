class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        # keep track of index and accumulator 
        def dfs(i, curr, total):

            # base case
            if total == target:
                res.append(curr.copy())
                return 
            
            # base case - soln not found
            if i >= len(nums) or total > target:
                return 

            curr.append(nums[i])
            # traverse the tree
            # first we explore left most num[i]
            dfs(i, curr, total + nums[i])

            # undo and explore right branch
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res