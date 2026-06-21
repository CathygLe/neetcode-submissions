class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)

        output = 0

        for c in letters:
            l = r = replacements = 0 

            while r < len(s):
                if s[r] != c:
                    replacements += 1
                
                while replacements > k and l < r:
                    if s[l] != c:
                        replacements -= 1
                    l += 1
                output = max(output, r-l+1)
                r += 1
            
        return output
                


        
                    
