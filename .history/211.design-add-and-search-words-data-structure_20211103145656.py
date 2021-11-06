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
        curr=self.root
        for c in word:
            curr=curr.children[c]
        curr.is_word=True

    def search(self, word: str) -> bool:
        curr=self.root
        self.res = False
        self.dfs(curr, word)
        return self.res

    def dfs(self, node, word):
        if word is None:
            self.res=True
            return 

        if word[0]==".":
            stack = node.children
            print(stack)
            while stack:
                queue=stack.pop()
                return self.dfs(queue, word[1:])
        else:
            node=node.children.get(word[0])
            if node is None:
                self.res=False
                return 
            if node.is_word==True:
                self.res=True
                return 
            return self.dfs(node, word[1:])


            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

