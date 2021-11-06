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

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None 

        isValid=True
        while root.left or root.right:
            if self.dfs(root)==False:
                isValid=False
                break
            else:
                return self.isValidBST(root.left) or self.isValidBST(root.right)
        
        return isValid

        
    def dfs(self, node):
        if node.left and node.right:
            if node.left.val < node.val and node.val < node.right.val:
                return True
            else:
                return False
        if node.left and not node.right:
            if node.left.val < node.val:
                return True
            else:
                return False
        if not node.left and node.right:
            if node.val < node.right.val:
                return True
            else:
                return False
# @lc code=end

