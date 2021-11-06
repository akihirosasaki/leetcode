#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans,level = [],0
        self.dfs(root,level,ans)
        return ans
    
    def dfs(self, root, level, ans):
        if not root:
            return
        if len(ans) < level+1:
            ans.append([])
        ans[level].append(root.val)
        self.dfs(root.left, level+1, ans)
        self.dfs(root.right, level+1, ans)
# @lc code=end

