class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= k:
            return [max(nums)]

        window = []
        count = 0
        result = []

        for r in range(len(nums)):
            window.append(nums[r])
            count += 1

            if count > k:
                window.pop(0)
                count -= 1

            if count == k:
                result.append(max(window))

        return result



        
        