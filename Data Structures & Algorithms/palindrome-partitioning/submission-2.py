class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def dfs(i, path):

            # base case
            if i >= len(s):
                res.append(path)
                return 

            for j in range(i, len(s)):
                if isPal(i, j):
                    dfs(j + 1, path + [s[i:j+1]])

        dfs(0, [])
        return res