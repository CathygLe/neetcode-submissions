class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for i, let in enumerate(s):
            mapS[let] = mapS.get(let, 0) + 1
        
        for i, let in enumerate(t):
            mapT[let] = mapT.get(let, 0) + 1

        return True if mapS == mapT else False