#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
"""My Answer"""
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return None 

#         isValid=True
#         isValid_left=True
#         isValid_right=True
#         while root.left or root.right:
#             if root.left:
#                 isValid_left=self.dfs_left(root)
#             if root.right:
#                 isValid_right=self.dfs_right(root)
#             if isValid_left==False or isValid_right==False:
#                 isValid=False
#                 break
#             else:
#                 return self.isValidBST(root.left) or self.isValidBST(root.right)
        
#         return isValid

        
#     def dfs_left(self, node):
#         if not node.left:
#             return True

#         isValid=True
#         if node.val<=node.left.val:
#             return False

#         while node.left.left or node.left.right:
#             if node.left.left:
#                 if node.val<=node.left.left.val:
#                     isValid=False
#                     break
#                 self.dfs_left(node.left.left)
#             if node.left.right:
#                 if node.val<=node.left.right.val:
#                     isValid=False
#                     break
#                 self.dfs_left(node.left.right)

#         return isValid

#     def dfs_right(self, node):
#         if not node.right:
#             return True

#         isValid=True
#         if node.val>=node.right.val:
#             return False

#         while node.right.left or node.right.right:
#             if node.right.left:
#                 if node.val>=node.right.left.val:
#                     isValid=False
#                     break
#                 self.dfs_right(node.right.left)
#             if node.right.right:
#                 if node.val>=node.right.right.val:
#                     isValid=False
#                     break
#                 self.dfs_right(node.right.right)            
        
#         return isValid

"""Similar Answer"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, lower, upper):
            
            if not node:
				# empty node or empty tree
                return True
            
            if lower < node.val < upper:
				# check if all tree nodes follow BST rule
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            
            else:
				# early reject when we find violation
                return False
            
        # ----------------------------------
        
        return helper( node=root, lower=float('-inf'), upper=float('inf') )
# @lc code=end
