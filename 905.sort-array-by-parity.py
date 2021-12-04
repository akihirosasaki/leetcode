#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        fast,slow=1,0
        while fast<len(nums):
            if  nums[slow]%2!=0 and nums[fast]%2==0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
            elif nums[slow]%2==0 and nums[fast]%2!=0:
                fast+=1
                slow+=1
            elif nums[slow]%2!=0 and nums[fast]%2!=0:
                fast+=1
            elif nums[slow]%2==0 and nums[fast]%2==0:
                fast+=2
                slow+=2
            
        return nums
# @lc code=end

