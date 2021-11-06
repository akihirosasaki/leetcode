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

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for dict in dictionary:
            self.root.insert(dict)
        
        stack = sentence.split('')
        curr=self.root
        while sentence_list:
            for c in word:

            curr=curr.children[c]


# @lc code=end

