#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=1
        while n*n<=num:
            if n*n==num:
                return True
            n+=1
        return False
# @lc code=end

