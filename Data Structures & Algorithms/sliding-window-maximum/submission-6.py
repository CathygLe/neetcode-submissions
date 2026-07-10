class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        maxsf = deque()
        l = 0 

        for r in range(len(nums)):
            while maxsf and nums[r] > nums[maxsf[-1]]:
                maxsf.pop()
            maxsf.append(r)

            if l > maxsf[0]:
                maxsf.popleft()

            if (r+1) >= k:
                output.append(nums[maxsf[0]])
                l += 1
        return output
