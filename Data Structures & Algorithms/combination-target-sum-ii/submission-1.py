class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, curr, total):
            # base case total == target
            if total == target:
                res.append(curr.copy())
                return

            # base case: greater than or out of bounds
            if i >= len(candidates) or total > target:
                return 

            #include candidate[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            #do not include candidate[i]
            curr.pop()
            #seach for non repeat
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res