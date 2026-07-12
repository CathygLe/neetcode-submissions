class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        front = 0 
        substring = set()
        result = 0 

        for i in range(len(s)):
            letter = s[i]

            while letter in substring:
                substring.remove(s[front])
                front += 1
            substring.add(letter)

            result = max(result, i - front + 1)

        return result 





            
            