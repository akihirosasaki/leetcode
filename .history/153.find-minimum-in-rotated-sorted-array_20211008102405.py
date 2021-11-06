#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None

        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0]

        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid]<nums[-1]:
                high=mid-1
            else:
                low=mid+1
# @lc code=end

