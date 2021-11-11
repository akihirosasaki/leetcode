#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset=set()
        i=0
        for j in jewels:
            hashset.add(j)
        for s in stones:
            if s in hashset:
                i+=1
        return i
# @lc code=end

