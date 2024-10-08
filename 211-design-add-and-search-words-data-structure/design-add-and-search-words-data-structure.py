class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isWord = True        

    def search(self, word: str) -> bool:

        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                letter = word[i]
                if letter == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else: 
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]
            return curr.isWord

    
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)