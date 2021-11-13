#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        if sum(nums[1:])==0:
            return 0
        for i in range(1,len(nums)-1):
            left=self.calc(nums,i)
            right=total-self.calc(nums,i+1)
            if left==right:
                return i
        if sum(nums[:-1])==0:
            return len(nums)-1
        return -1

    def calc(self, nums: List[int], idx: int):
        return sum(nums[:idx])
# @lc code=end

