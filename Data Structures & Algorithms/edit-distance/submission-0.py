class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        #                       Word 2
        # grid will look like [inf, inf, 3]
        #          Word1      [inf, inf, 2]
        #                     [inf, inf, 1]
        #                     [2  , 1  , 0]
        
        # initialize the edge cases 
        for j in range(len(word2)+1):
            # starting at end of word1 > empty string 
            cache[len(word1)][j] = len(word2) - j 

        for i in range(len(word1) + 1):
            # starting at end of word2 > empty string
            cache[i][len(word2)] = len(word1) - i


        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]

                # check all cases (delete, insert, replace)
                else: 
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]

        