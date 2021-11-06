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
        isValid_left=True
        isValid_right=True
        left_list=[]
        right_list=[]
        while root.left or root.right:
            if root.left:
                isValid_left=self.dfs_left(root, left_list)
            if root.right:
                isValid_right=self.dfs_right(root, right_list)
            if isValid_left==False or isValid_right==False:
                isValid=False
                break
            else:
                return self.isValidBST(root.left) or self.isValidBST(root.right)
        
        return isValid

        
    def dfs_left(self, node, list):
        list.append(node.left.val)
        while node.left.left or node.left.right:
            list.append(node.left.left.val)
            list.append(node.left.right.val)
            self.dfs_left(node.left.left, list)
            self.dfs_left(node.left.right, list)
        isValid=True
        for num in list:
            if node.val <= num:
                isValid=False
                break
        return isValid

    def dfs_right(self, node, list):
        list.append(node.right.val)
        while node.right.left or node.right.right:
            list.append(node.right.left.val)
            list.append(node.right.right.val)
            self.dfs_right(node.right.left, list)
            self.dfs_right(node.right.right, list)
        isValid=True
        for num in list:
            if node.val >= num:
                isValid=False
                break
        return isValid
                
# @lc code=end
