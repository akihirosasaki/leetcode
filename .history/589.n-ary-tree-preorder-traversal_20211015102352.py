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
    order=[]
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        self.order.append(root.val)
        for child in root.children:
            self.preorder(child)
        return self.order
        
# @lc code=end

