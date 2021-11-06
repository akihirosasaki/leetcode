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

class Solution:
    out = []
    def preorder(self, root: 'Node') -> List[int]:
        def helper(root):
            if not root:
                return None
            self.out.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return self.out
# @lc code=end

