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
            if key<curr.val:
                prev=curr
                curr=curr.left
            if key>curr.val:
                prev=curr
                curr=curr.right

            if curr.val==key:
                if curr.left and curr.right:
                    if curr.val>prev.val:
                        prev.right=curr.left
                        curr.left.right=curr.right
                elif curr.left and not curr.right:
                    if curr.val>prev.val:
                        prev.right=curr.left
                    else:
                        prev.left=curr.left
                elif not curr.left and curr.right:
                    if curr.val>prev.val:
                        prev.right=curr.right
                    else:
                        prev.left=curr.right
                else:
                    if curr.val>prev.val:
                        prev.right=None
                    else:
                        prev.left=None
            return root
                


        
# @lc code=end

