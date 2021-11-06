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
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr=curr.children[c]
        curr.points = val

    def sum(self, prefix: str) -> int:
        res = 0
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        stack = []
        stack.append(curr)
        while stack:
            x = stack.pop()
            res += x.points
            stack.extend(x.children.values())
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

