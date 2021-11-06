#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        if n>=2:
            joinList = self.grammarList(n)
            return joinList[k-1]

    def grammarList(self, n:int):
        if n==1:
            return 0
        if n>=2:
            strVal = self.grammarList(n-1)
            list=[]
            for str in strVal:
                if str==0:
                    list.append("01")
                if str==1:
                    list.append("10")
            joinList = ','.join(list)
            return joinList

# @lc code=end

