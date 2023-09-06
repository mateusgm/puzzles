# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.all  = {}
        self.tree = {}

    def addWord(self, word: str) -> None:
        self.all[word] = True

        node = self.tree
        for c in word:
            if c in node:
                node = node[c]
            else:
                node[c] = { }
                node = node[c]
        node['exact'] = True

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.all

        return self.searchSubTree(word, self.tree)


    def searchSubTree(self, word: str, node: dict) -> bool:
        if word == '':
            return 'exact' in node

        letter = word[0]

        if letter != '.':
            if letter not in node:
                return False
            else:
                return self.searchSubTree(word[1:], node[letter])

        result = False
        for k in node.keys():
            if k == 'exact':
                continue
            result = result or self.searchSubTree(word[1:], node[k])

        return result



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)