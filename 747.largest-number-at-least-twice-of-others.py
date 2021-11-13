#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        maxNumKey=nums.index(max(nums))
        maxNum=nums.pop(maxNumKey)
        nums2x = [n*2 for n in nums]
        if maxNum>=max(nums2x):
            return maxNumKey
        else:
            return -1
# @lc code=end

