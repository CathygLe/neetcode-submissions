class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copies = set()


        for num in nums:
            if num in copies:
                return True 
            copies.add(num)
        
        return False 
        