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
        lists=[]
        listLength=0
        while len(nums)>0:
            num = nums.pop()
            lists=self.helper(lists, num, listLength)
            listLength+=1
        return lists

    def helper(self, preLists: List[List[int]], num: int, listLength: int):
        newLists=[]
        if listLength==0:
            newLists.append(list(num))
        else:    
            for preList in preLists:
                newList=preList
                for idx in range(listLength):
                    newList.insert(idx,num)
                    newLists.append(newList)
        return newLists

        

# @lc code=end

