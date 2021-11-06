#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return None

        bracketList=[]
        bracketList.append("()")
        while n>1:
            bracketList = self.addBrackets(bracketList)
            n-=1

        return bracketList

    def addBrackets(self, list):
        newList=[]
        for str in list:
            newList.append(str+"()")
            newList.append("()"+str)
            newList.append("("+str+")")
        return list(set(newList))
# @lc code=end
