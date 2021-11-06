#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            curr=curr.children[c]
        curr.is_word=True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for target in dictionary:
            self.root.insert(target)
        
        stack=sentence.split('')
        output=[]
        while stack:
            curr=self.root
            word=stack.pop()
            for c in word:
                if curr.is_word is True:
                    output.insert(0, curr)
        return ' '.join(output)
        


# @lc code=end

