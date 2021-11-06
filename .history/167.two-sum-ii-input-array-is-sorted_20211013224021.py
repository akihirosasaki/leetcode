#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        while len(numbers)>0:
            i+=1
            num = numbers.pop(0)
            result = self.binarySearch(num, numbers, target, i)
            print(num, result)
            if result!=-1:
                return [i, result]



    def binarySearch(self, num: int, nums: List[int], target: int, idx: int):
        if not nums:
            return None

        if len(nums)==1:
            return idx+1
        if len(nums)==2:
            if nums[0]+num==target:
                return idx+1
            elif nums[0]+num<target:
                if nums[1]+num==target:
                    return idx+2
                else:
                    return -1
                

        
        l,r=0, len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]+num==target:
                return m+idx+1
            elif nums[m]+num<target:
                l=m+1
            else:
                r=m
        return -1
# @lc code=end

