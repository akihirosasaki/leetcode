#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            print(i,nums)
            if nums[i]==0 and nums[i+1]!=0:
                nums[i]=nums[i+1]
                nums[i+1]=0
            
                

# @lc code=end

