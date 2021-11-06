#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans,level = [],0
        self.dfs(root,level,ans)
        return ans

    def dfs(self, root, level, ans):
        if not root:
            return None
        if len(ans) < level+1:
            ans.append([])
        ans[level].append(root.val)
        for child in root.children:
            self.dfs(child, level+1, ans)
# @lc code=end

