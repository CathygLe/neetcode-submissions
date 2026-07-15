class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #logn time tells us we want to split the problem in half each time 
        # therefore, we'll check if its on the left or right side... 

        l = 0 
        r = len(nums) - 1

        while l <= r: 
            mid = l + (r-l)//2 

            if target == nums[mid]:
                return mid 
            elif nums[l] <= nums[mid]:
                if nums[mid] >= target and nums[l] <= target:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                if nums[mid] <= target and nums[r]>= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

