#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans, depth = 0, 1
        ans = self.searchMaxDepth(root, ans, depth)
        return ans
    
    def searchMaxDepth(self, root, ans, depth):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return max(ans, depth)
        ans_l = self.searchMaxDepth(root.left, ans, depth+1)
        ans_r = self.searchMaxDepth(root.right, ans, depth+1)
        return max(ans_l, ans_r)
        
# @lc code=end

