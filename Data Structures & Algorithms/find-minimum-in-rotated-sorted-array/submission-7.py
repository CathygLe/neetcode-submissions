class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1


        # 1 2 3 4 5 
        # 2 3 4 5 1 
        # 4 5 1 2 3

        while l < r:
            mid = l + (r-l) // 2 
            ## left is sorted 
            
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
            
        


            
        