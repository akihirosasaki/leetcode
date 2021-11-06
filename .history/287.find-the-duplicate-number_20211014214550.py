#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None

        sum1=0
        sum2=0
        for i in range(1, len(nums)):
            sum1+=i
        for j in nums:
            sum2+=j
        return sum2-sum1
# @lc code=end

