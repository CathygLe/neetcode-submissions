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

            result = max(result, len(substring))
        return result 






            
            