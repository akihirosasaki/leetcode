#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        memo={}
        return self.dfs(nums,target,memo)

    def dfs(self, nums, target, memo):
        print(memo)
        if tuple(nums+[target]) in memo:
            return memo[tuple(nums+[target])]
        if not nums:
            if target==0:
                return 1
            return 0
        cnt=0
        cnt+=self.dfs(nums[1:], target-nums[0], memo)
        cnt+=self.dfs(nums[1:], target+nums[0], memo)
        memo[tuple(nums+[target])]=cnt
        return cnt
        
# @lc code=end

