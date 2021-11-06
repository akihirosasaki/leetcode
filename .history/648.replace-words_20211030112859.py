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
        self.is_word = False
    
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            curr=curr.children[c]
        curr.is_word=True

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
            result=self.root.startsWith(word)
            if result is True:
                pass


# @lc code=end

