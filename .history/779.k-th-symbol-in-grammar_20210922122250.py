#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start

memo=[-1]*31

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:     
        memo[n] = self.grammarList(n)
        print(memo)
        return memo[n][k-1]

    def grammarList(self, n:int):
        if n==1:
            memo[n-1]="0"
            return memo[n-1]
        if n>=2:
            strVal=""
            if memo[n-1]!=-1:
                strVal=memo[n-1]
            else:
                strVal=memo[n-1]=self.grammarList(n-1)
            list=[]
            for str in strVal:
                if str=="0":
                    list.append("01")
                if str=="1":
                    list.append("10")
            memo[n] = ''.join(list)
            return memo[n]

# @lc code=end

