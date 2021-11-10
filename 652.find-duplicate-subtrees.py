# @before-stub-for-debug-begin
from python3problem652 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d=DefaultDict(int)
        output=[]

        def dfs(node):
            if not node:
                return 
            s=tuple([dfs(node.left),node.val,dfs(node.right)])
            if d[s]==1:
                output.append(node)
            d[s]+=1
            return s
            
        dfs(root)
        return output
# @lc code=end
