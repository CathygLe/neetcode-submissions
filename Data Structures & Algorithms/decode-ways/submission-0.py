class Solution:
    def numDecodings(self, s: str) -> int:
        # base case: empty string 
        dp = {len(s): 1}

        def dfs(i):
            # if at the end, we have a combo!
            if i in dp:
                return dp[i]
            
            # if starts with 0, not valid
            if s[i] == "0":
                return 0
            
            # check the next letter
            res = dfs(i + 1)

            # check if we have 2 digit 
            # in bound and starts w/ 1 or 2 w/ 0-6
            if (i + 1 <len(s) and (s[i]== "1" or 
                s[i]== "2" and s[i+1] in "0123456")):

                # check for more combos after
                res += dfs(i + 2)

            # store the # of combos computed at index i 
            # so we don't recompute when we do i-1 and check i + 1
            dp[i] = res

            return res 
        return dfs(0)
                