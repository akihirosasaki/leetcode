#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution_rec:
    def __init__(self):
        self.order = []
    def rec(self, root) -> List[int]:
        if root is None: return
        self.order.append(root.val)
        for child_node in root.children:
            self.preorder(child_node)
    def preorder(self, root) -> List[int]:
        self.rec(root)
        return self.order
        
# @lc code=end

