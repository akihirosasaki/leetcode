#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset=set()
        for n in nums:
            if (n not in hashset):
                hashset.add(n)
            else:
                hashset.remove(n)
        return hashset.pop()
# @lc code=end

