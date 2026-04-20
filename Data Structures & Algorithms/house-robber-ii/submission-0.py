class Solution:
    def rob(self, nums: List[int]) -> int:

        # we can treat the problem like house robber 1
        # Break the problem into 2, either return index
        n = len(nums)

        def houseR(nums):
            rob1 = 0
            rob2 = 0

            for num in nums:
                temp = max(rob1 + num, rob2)

                rob1 = rob2
                rob2 = temp 
            
            return rob2
            
        return max(houseR(nums[:n-1]), houseR(nums[1:]))




        