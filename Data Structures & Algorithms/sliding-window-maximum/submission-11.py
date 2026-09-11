class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
 
        mono = deque()

        left = 0 

        for right in range(len(nums)):
            
            while mono and nums[right] > nums[mono[-1]]:
                mono.pop()
            mono.append(right)

            if mono[0] < left:
                mono.popleft()

            if right + 1 >= k:
                output.append(nums[mono[0]])
                left += 1
            
        return output 



