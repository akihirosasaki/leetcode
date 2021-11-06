#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high=0,len(nums)
        mid=(high+low)/2
        while high-low>1:
            count=0
            for k in nums:
                if mid < k <= high:
                    count+=1
            if count > high - mid:
                low=mid
            else:
                high=mid
            mid=(high+low)/2
        return high
# @lc code=end

