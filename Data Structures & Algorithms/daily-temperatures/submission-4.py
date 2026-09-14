class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = len(temperatures) * [0]
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, t = stack.pop()
                result[i] = index - i 
            stack.append([index,temp])
        return result 
        