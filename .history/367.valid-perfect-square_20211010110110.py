#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return true

        l,r=0,num
        while l+1<r:
            mid=(l+r)//2
            if mid*mid<num:
                l=mid
            elif mid*mid>num:
                r=mid
            else:
                return True
        return False

# @lc code=end

