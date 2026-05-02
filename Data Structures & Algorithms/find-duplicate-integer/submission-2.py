class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0 

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if nums[slow] == nums[fast]:
                break


        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                break
            
        return slow2