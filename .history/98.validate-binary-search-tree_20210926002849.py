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

memo = []
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None

        while root.left or root.right:
            if self.dfs(root)==False:
                return False
            else:
                return self.isValidBST(root.left) or self.isValidBST(root.right)
            

        
    def dfs(self, node):
        if not node.left or not node.right:
            return False
        else:
            print(node.left.val)
            print(node.val)
            print(node.right.val)
            if node.left.val < node.val and node.val < node.right.val:
                return True
            else:
                return False
# @lc code=end

