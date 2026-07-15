class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #   l   m   r   target = 2 
        # [ 1 2 3 4 5 ]  l = 1, r = 5 m = 3  target < mid     r = mid - 1
        # [ 1 2 3 ]      l = 1  r = 2  mid = 2   

        # [ 4 5 1 2 3 ]  l = 4, r = 3 mid = 1    target > mid 
        # [ 2 3 4 5 1 ]

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

