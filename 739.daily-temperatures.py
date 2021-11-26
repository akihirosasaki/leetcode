#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temperature:
                cur=stack.pop()
                ans[cur]=i-cur
            stack.append(i)
                    
        return ans
# @lc code=end

