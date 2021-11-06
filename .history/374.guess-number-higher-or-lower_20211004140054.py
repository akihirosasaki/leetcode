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
        if n==2:
            if guess(n)==-1:
                return 1
            else:
                return 2
        
        mid = n//2+1

        result=guess(mid)
        if result==-1:
            n=mid
        elif result==1:
            n=(mid+n)//2
        else:
            return mid
        
        return self.guessNumber(n)
# @lc code=end

