class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 

        char = set(s)


        for c in char:
            l = r = replacement = 0 

            while r < len(s):
                if s[r] != c:
                    replacement += 1
                

                while l < r and replacement > k:
                    if s[l] != c:
                        replacement -= 1
                    l += 1
               
                res = max(res, r-l + 1 )
                r += 1
        return res 
                    
