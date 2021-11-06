#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.root=Node()
        self.children = self.root.children
        self.is_word = self.root.is_word
    
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            curr=curr.children[c]
        curr.is_word=True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root=TrieNode()
        for target in dictionary:
            root.insert(target)
        
        stack=sentence.split(' ')
        output=[]
        while stack:
            curr=root
            word=stack.pop()
            for c in word:
                if curr.is_word is True:
                    output.insert(0, curr)
                curr=curr.children[c]
        print(output)
        return ' '.join(output)
        


# @lc code=end

