class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        substring = set()

        first = 0 
        result = 0
        
        for i in range(len(s)):

            while s[i] in substring:
                substring.remove(s[first])
                first += 1
            substring.add(s[i])
            
            length = i - first + 1

            result = max(result, length)

        return result 




            
            