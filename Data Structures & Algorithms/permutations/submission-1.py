class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []


        def backtrack(curr, remaining):
            if not remaining:
                result.append(curr)
                return
            

            for i in range(len(remaining)):
                val = remaining[i]

                backtrack(curr + [val], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return result