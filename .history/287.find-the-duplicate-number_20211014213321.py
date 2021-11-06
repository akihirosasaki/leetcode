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
        queue=nums.pop()
        if queue in list:
            return queue
        else:
            list.append(queue)
# @lc code=end

