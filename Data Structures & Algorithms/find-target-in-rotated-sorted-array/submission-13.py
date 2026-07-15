class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            ## check if mid is the solution 
            if target == nums[mid]:
                return mid
            
            ## Check if the left is sorted 
            if nums[l] <= nums[mid]:
                ## if the left is sorted, check if the target is in the right 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                ## else target is on the right side 
                else:
                    r = mid - 1
            ## since the left side wasn't sorted, the right side must be sorted 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 
                else: 
                    l = mid + 1 
        return -1 