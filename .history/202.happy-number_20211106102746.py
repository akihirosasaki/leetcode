#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n<=0:
            return False
        nlist=[int(d) for d in str(n)]
        
# @lc code=end

