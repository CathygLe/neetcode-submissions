class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        start = 0 
        best = 0 

        for i in range(len(s)):
            while s[i] in curr:
                curr.remove(s[start])
                start +=1

            curr.add(s[i])
            best = max(best, len(curr))
            
        return best 
