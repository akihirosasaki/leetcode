#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i,k in enumerate(s):
            if k not in d.keys():
                d[k]=[i, True]
            else:
                d[k][1]=False
        print(d.values()[1]==True)
# @lc code=end

