#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.points = 0

class MapSum:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr=self.root
        for c in key:
            curr=curr.children[c]

    def sum(self, prefix: str) -> int:
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

