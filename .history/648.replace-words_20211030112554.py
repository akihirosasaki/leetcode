#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = {}
    
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            curr=curr.children[c]

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            curr=curr.children.get(c)
            if curr is None:
                return False
        return True

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for target in dictionary:
            self.root.insert(target)
        
        stack = sentence.split('')
        while stack:
            word = stack.pop()
            self.root.startsWith(word)


# @lc code=end

