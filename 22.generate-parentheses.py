#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
# my answer
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n==0:
#             return None

#         bracketList=[]
#         bracketList.append("()")
#         while n>1:
#             bracketList = self.addBrackets(bracketList)
#             n-=1

#         return bracketList

#     def addBrackets(self, bracketList):
#         newList=[]
#         for str in bracketList:
#             newList.append(str+"()")
#             newList.append("()"+str)
#             newList.append("("+str+")")
#         return list(set(newList))

# similar answer
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfs(n, n, "", res)
        return res
            
    def dfs(self, leftRemain, rightRemain, path, res):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return  # backtracking
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
            return 
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)
# @lc code=end
