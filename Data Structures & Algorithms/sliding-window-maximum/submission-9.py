class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        mono = deque()

        left = 0 

        for right in range(len(nums)):
            num = nums[right]

            while mono and num > nums[mono[-1]]:
                mono.pop()
            mono.append(right)

            while mono[0] < left:
                mono.popleft()
                
            if right + 1 >= k: 
                output.append(nums[mono[0]])
                left += 1
    
        return output
            



