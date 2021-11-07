#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1,d2={},{}
        for i,k in enumerate(list1):
            d1[k]=i
        for i,k in enumerate(list2):
            if k in d1.keys():
                d2[k]=i+d1[k]
        return [k for k, v in d2.items() if v == min(d2.values())]
        
# @lc code=end

