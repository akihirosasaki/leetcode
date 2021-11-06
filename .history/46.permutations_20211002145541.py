# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        i = nums.pop()

        def helper(self, preLists: List[List[int]], i: int):
            newLists=[]
            listLength=len(preLists[0])
            for preList in preLists:
                newList=preList
                for idx in range(listLength):
                    newList.insert(idx,i)
                    newLists.append(newList)
            return newLists


# @lc code=end

