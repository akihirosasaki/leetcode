#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        output=[]
        while k>0:
            m = max(d, key=d.get)
            output.append(m)
            del d[m]
            k-=1
        return output
# @lc code=end

