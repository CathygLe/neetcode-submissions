class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono = deque()
        left = 0 
        output = []

        for i in range(len(nums)):

            while mono and nums[mono[-1]] < nums[i]:
                mono.pop()
            mono.append(i)

            if left > mono[0]:
                mono.popleft()

            if i + 1 >= k:
                output.append(nums[mono[0]])
                left += 1 
        return output 





