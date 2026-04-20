class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # base case 
        if len(nums) == 0:
            return [[]]
        
        # get list of all permutations exluding first element
        perms = self.permute(nums[1:])

        res = []

        for p in perms:
            # insert the first element into each ith place
            for i in range(len(p) + 1):
                p_copy = p.copy()  # Make a copy to avoid modifying the original list
                p_copy.insert(i, nums[0])  # Insert nums[0] at position i
                res.append(p_copy)  # Add the new permutation to the result list
        
        return res  # Return the full list of permutations

