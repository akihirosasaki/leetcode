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

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for dict in dictionary:
            self.root.insert(dict)
        
        sentence_list = sentence.split('')
        for word in sentence_list:
            for c in word:

# @lc code=end

