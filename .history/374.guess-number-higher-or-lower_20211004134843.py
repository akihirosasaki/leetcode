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
        print(n)
        result=self.guess(n)
        if result==-1:
            n-=1
        elif result==1:
            n+=1
        else:
            n
        
        return self.guessNumber(n)
# @lc code=end

