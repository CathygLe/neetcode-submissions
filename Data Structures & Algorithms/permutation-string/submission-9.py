class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word1 =  {}

        for let in s1:
            word1[let] = word1.get(let,0) + 1 
        

        for i in range(len(s2)-len(s1)+1):
            word2 = {}

            for check in range(i, i+len(s1)):
                letter = s2[check]

                word2[letter] = word2.get(letter,0) + 1

                if word2[letter] > word1.get(letter,0):
                    break 
                
                if word2 == word1:
                    return True
        return False




        