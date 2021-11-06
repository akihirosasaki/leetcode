#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return -1

        length=len(nums)
        midIdx=length//2
        if nums[midIdx] > target:
            nums = nums[:midIdx]
        elif nums[midIdx] < target:
            nums = nums[midIdx+1:]
        else:
            return midIdx
        print(nums)
        return self.search(nums, target)

# @lc code=end

