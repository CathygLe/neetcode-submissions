class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        count = 0
        l = 0 
        
        if len(s) == 0:
            return count

        for letter in s:

            if letter in result:
                while letter in result: 
                    result.remove(s[l])
                    l += 1
                result.add(letter)
            else: 
                result.add(letter)
                count = max(count, len(result))

        return count


            
            