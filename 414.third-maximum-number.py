#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start

import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hashset=set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
        hashlist=list(hashset)
        if len(hashlist)<3:
            return max(hashlist)
        return min(heapq.nlargest(3,hashlist))

# @lc code=end

