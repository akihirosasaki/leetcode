#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        node=self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        print(word)
        if not word:
            if node.isWord:
                self.res=True
            return 

        if word[0]==".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node=node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

