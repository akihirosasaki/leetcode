#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        queue=[]
        queue.append(root)
        if key < root.val:
            self.deleteNode(root.left, key)
        elif key > root.val:
            self.deleteNode(root.right, key)
        else:

# @lc code=end

