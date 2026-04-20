class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        elif set(s) != set(t):
            return False
        else:   
            sMap = {} 
            tMap = {}

            for letter in s:
                if letter in sMap:
                    sMap[letter] += 1
                else: 
                    sMap[letter] = 1
            
            for letter in t:
                if letter in tMap:
                    tMap[letter] +=1 
                else: 
                    tMap[letter] = 1

            return tMap == sMap 



        