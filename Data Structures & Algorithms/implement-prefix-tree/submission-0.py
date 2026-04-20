class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        # create an empty tree
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # start at the root
        curr = self.root

        # for each letter
        for c in word: 
            # if the letter is not added, create a new trienode
            if c not in curr.children:
                curr.children[c] = TrieNode()
            #else if exists, move current 
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        # check if its the end of word
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        # end of word has reached
        return True
        
        