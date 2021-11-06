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
            tmpList=[]
            tmpList.append(num)
            newLists.append(tmpList)
        else:    
            for preList in preLists:
                print(preList)
                newList=preList
                print(newList)
                for idx in range(listLength+1):
                    newList.insert(idx,num)
                    print(newList)
                    newLists.append(newList)
        return newLists

        

# @lc code=end

