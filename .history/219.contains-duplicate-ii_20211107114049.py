#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,key in enumerate(nums):
            if key not in d.keys():
                d[key]=[i,False]
            else:
                if d[key][1]==False:
                    d[key]=[i-d[key][0],True]
                else:
                    if (i-d[key][0]) < d[key][0]:
                        d[key]=[i-d[key][0],True]
                
        for n in d.values():
            if n[0]<=k and n[1]==True:
                return True
        return False
                
# @lc code=end

