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
        for c in word:
            if c==".":
                list=curr.children.keys()
                curr
            else:
                curr=curr.children.get(c)
            if curr is None:
                return False
        return curr.is_word

        def __helper(node: TrieNode, c: str):
            curr=node
            if c==".":
                keyList=curr.children.keys()
                for i in keyList:
                    curr=curr.children.get(i)
                    return __helper(curr, )
            else:
                curr=curr.children.get(c)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

