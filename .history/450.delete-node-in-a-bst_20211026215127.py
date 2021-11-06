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
        if not root:
            return None

        prev, curr=TreeNode(-1),root
        while curr:
            if val<curr.val:
                curr=curr.left
            if val>curr.val:
                curr=curr.right

            if curr.val==val:
                if curr.left or curr.right:

                


        
# @lc code=end

