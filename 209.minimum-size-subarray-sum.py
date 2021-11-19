#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        output=[]
        fast,slow=1,0
        while fast>slow:
            if sum(nums[slow:fast])<target:
                if fast<=len(nums): 
                    fast+=1
                else:
                    break
            else:
                output.append(len(nums[slow:fast]))
                slow+=1
        return min(output)
# @lc code=end

