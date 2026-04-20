class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s2Map = {}
        for letter in s1:
            if letter in s2Map:
                s2Map[letter] +=1
            else:
                s2Map[letter] = 1
        
        checkMap = {}
        for letter in s2:
            if letter in s2Map:
                checkMap[letter] = 1 + checkMap.get(letter, 0)
                checkCount = checkMap[letter]
                letterCount = s2Map[letter]

                if checkCount > letterCount:
                    checkMap = {}
                    break;
            else:
                checkMap = {}

            if checkMap == s2Map:
                return True
        return False 


        





        