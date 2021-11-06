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

        list=[]
        list.append("()")
        while n>1:
            list = self.addBrackets(list)
            n-=1

        return list
        
    def addBrackets(self, list):
        newList=[]
        for str in list:
            newList.append(str+"()")
            newList.append("()"+str)
            newList.append("("+str+")")
        return set(newList)
# @lc code=end

