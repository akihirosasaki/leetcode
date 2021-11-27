#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# my answer
# class Solution:
#     visited={}
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         self.dfs(node)
#         for key in self.visited.keys():
#             return Node(key, self.visited[key])
        

#     def dfs(self,n: 'Node'):
#         if not n:
#             return 
#         if n in self.visited.keys():
#             return
#         if not n.neighbors:
#             return []
#         self.visited[n]=n.neighbors
#         for neighbor in n.neighbors:
#             self.dfs(neighbor)
# DFS recursively
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

    
# @lc code=end

