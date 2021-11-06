#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        curr=1
        while curr*curr < x:
            curr+=1
        return curr-1

# @lc code=end

