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

        list = []
        while nums:
            num=nums.pop()
            if num in list:
                return num
            else:
                list.append(num)
# @lc code=end

