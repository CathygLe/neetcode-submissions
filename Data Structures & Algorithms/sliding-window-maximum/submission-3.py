class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # output = []
        # q = deque()  # stores indexes
        # l = r = 0


        # # queue will be storing the largest value at the front 
        # # Montotonically decreasing queue

        # while r < len(nums):
        #     # keep popping until the we can add nums[r]
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     if l > q[0]:
        #         q.popleft()

        #     # check if we have checked the whole window yet
        #     if (r + 1) >= k:
        #         output.append(nums[q[0]])
        #         l += 1
        #     r += 1

        # return output

        result = []
        for i in range(len(nums)-k+1):
            temp = [] 

            for j in range(i, i+k):
                temp.append(nums[j])

            result.append(max(temp))
        return result 
            




        
        