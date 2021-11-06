#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None

        if len(nums)==1:
            return 0

        for i in range(len(nums)-2):
            if nums[i]<nums[i+1] and nums[i+1]>nums[i+2]:
                return i+1

        return max(nums[0], nums[len(nums)-1])
            

# @lc code=end

