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
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None 

        isValid=True
        isValid_left=True
        isValid_right=True
        while root.left or root.right:
            if root.left:
                isValid_left=self.dfs_left(root)
            if root.right:
                isValid_right=self.dfs_right(root)
            if isValid_left==False or isValid_right==False:
                isValid=False
                break
            else:
                return self.isValidBST(root.left) or self.isValidBST(root.right)
        
        return isValid

        
    def dfs_left(self, node, list):
        if not node.left:
            return True

        isValid=True
        while node.left.left or node.left.right:
            if node.left.left:
                if node.val<=node.left.left.val:
                    isValid=False
                    break
                self.dfs_left(node.left.left, list)
            if node.left.right:
                if node.val<=node.left.right.val:
                    isValid=False
                    break
                self.dfs_left(node.left.right, list)
        

        return isValid

    def dfs_right(self, node, list):
        if not node.right:
            return True

        while node.right.left or node.right.right:
            if node.right.left:
                list.append(node.right.left.val)
                self.dfs_right(node.right.left, list)
            if node.right.right:
                list.append(node.right.right.val)
                self.dfs_right(node.right.right, list)            
        isValid=True

        return isValid
                
# @lc code=end
