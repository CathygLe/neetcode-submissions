class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for letter in s1:
            count1[letter] = count1.get(letter, 0) + 1
        

        for windowStart in range(len(s2)-len(s1)+1):
            count2={}

            for window in range(windowStart, windowStart+len(s1)):

                let = s2[window]

                count2[let] = count2.get(let, 0) + 1

                if count2[let] > count1.get(let, 0):
                    break 
                elif count2 == count1:
                    return True 
        return False 





        