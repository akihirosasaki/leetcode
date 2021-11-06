#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return None

        old, new=1,n
        mid=(old+new)//2
        while old<new:
            result=isBadVersion(mid)
            if result==True:
                new=mid
            else:
                old=mid+1

        return mid

        
# @lc code=end

