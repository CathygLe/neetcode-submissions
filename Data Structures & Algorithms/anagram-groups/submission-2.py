class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord in result:
                result[sortedWord].append(word)
            else: 
                result[sortedWord] = [word]

        final = result.values()

        return list(final) 



     
        