#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)==2:
            return True
        for n in arr:
            if n==0:
                continue
            if 2*n in arr:
                return True
        return False
# @lc code=end

