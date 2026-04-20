class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Constraints make this a linked list problem with nums = pointers
        # both start at 0 since 0 can't be the answer 
        # 0 can't be the answer because then the loop is at the beginning
        slow = 0
        fast = 0

        # find duplicate
        while True:
            slow = nums[slow]

            # this is similar to .next.next
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # return first node of duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        