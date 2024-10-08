class TrieNode:
    def __init__(self, val=-1):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        if curr.isWord == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)