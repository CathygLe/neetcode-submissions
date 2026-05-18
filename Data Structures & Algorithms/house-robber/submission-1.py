class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        # [rob1, rob2, n, n+1,...]
        for n in nums:
            # rob the max of n - 2 or n - 1
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp
        
        return rob2 