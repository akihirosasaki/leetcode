#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or not target:
            return None

    def binarySearch(num: int, nums: List[int], target: int, idx: int):
        if not nums:
            return None

        l,r=0, len(nums)-1
        while l+1<r:
            m=(l+r)//2
            if nums[m]+num==target:
                return 
# @lc code=end

