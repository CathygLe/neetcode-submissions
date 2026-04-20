class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        sub = set()
        result = 0

        while r < len(s) - 1:
            if s[r] not in sub:
                sub.add(s[r])
                r += 1
            else:
                sub.remove(s[l])
                l += 1
            
            result = max(result, len(sub))
        return result
            