#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        return [expected[x]==heights[x] for x in range(len(heights))].count(0)
# @lc code=end

