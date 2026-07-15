class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # 1 2 3 4  mid = 
        # 4 1 2 3 
        # 2 3 4 1 

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]

            


            
        