#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root):
            if not root:
                return None
            for child in root.children:
                helper(child)
            out.append(root.val)
        out = []
        helper(root)
        return out
# @lc code=end

