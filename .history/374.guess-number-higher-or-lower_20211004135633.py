#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n//2

        result=guess(mid)
        if result==-1:
            n=mid
        elif result==1:
            n=(n+mid)//2
        else:
            return n
        
        return self.guessNumber(n)
# @lc code=end

