class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addChild(self, val):
        pass

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # spilt the sentence into words
        words = sentence.split(" ")

        for k, word in enumerate(words):
            minLen = 101
            for item in dictionary:
                i = 0
                root = ""
                if word[i] == item[i]:
                    if len(word) < len(item):
                        breakAt = len(word)
                    else:
                        breakAt = len(item)
                    while word[i] == item[i]:
                        root += item[i]
                        i += 1
                        if i > breakAt-1:
                            break
                    rootLength = len(root)
                    if rootLength == len(item):
                        if rootLength < minLen:
                            minLen = rootLength
                            shortestRoot = root
                        words[k] = shortestRoot
        print(words)
        return " ".join(words)
