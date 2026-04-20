class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                topI, topT = stack.pop()
                result[topI] = index - topI 

            stack.append([index,temp])

        return result
        