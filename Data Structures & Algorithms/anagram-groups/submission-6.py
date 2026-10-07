class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}


        for word in strs: 
            sortedWord = "".join(sorted(word))

            if sortedWord in mapped:
                mapped[sortedWord].append(word)
            else:
                mapped[sortedWord] = [word]
        
        result = []
        for words in mapped.values():
            result.append(words)

        return result

        



     
        