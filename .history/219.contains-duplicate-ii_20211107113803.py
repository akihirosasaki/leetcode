#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,k in enumerate(nums):
            if k not in d.keys():
                d[k]=[i,False]
            else:
                if d[k][1]==False:
                    d[k]=[i-d[k][0],True]
                else:
                    if (i-d[k][0]) < d[k][0]:
                        d[k]=[i-d[k][0],True]
                
        for n in d.values():
            print(n[0],n[1])
            print(n[0]<=k, n[1]==True)
            if n[0]<=k and n[1]==True:
                return True
        return False
                
# @lc code=end

