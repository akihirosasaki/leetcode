#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,n in enumerate(nums):
            m=target-n
            if m in d:
                return [d[m],i]
            else:
                d[n]=i
        
# @lc code=end

