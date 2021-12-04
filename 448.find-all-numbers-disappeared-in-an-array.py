#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset=set(nums)
        for i in range(1,len(nums)+1):
            if i in hashset:
                hashset.remove(i)
            else:
                hashset.add(i)
        return list(hashset)
# @lc code=end

