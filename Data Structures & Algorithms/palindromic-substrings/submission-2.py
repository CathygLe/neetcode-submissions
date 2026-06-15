class Solution:
    def countSubstrings(self, s: str) -> int:
        ways = 0 

        if len(s) == 0:
            return 0 
        elif len(s) == 1:
            return 1

        for i in range(len(s)):
            
            l = i
            r = i 
            # odd palindromes 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ways += 1 
                l -= 1 
                r += 1


            # even palindromes 
            l = i-1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ways += 1 
                l -= 1 
                r += 1
        return ways 


        