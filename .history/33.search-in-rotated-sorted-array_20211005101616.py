#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    idx=0
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1

        mid = len(nums)//2
        
        if nums[mid]>target:
            if nums[0]<target:
                nums=nums[:mid]
            elif nums[0]>target:
                self.idx+=mid+1
                nums=nums[mid+1:]
            else:
                return self.idx
        elif nums[mid]<target:
            self.idx+=mid+1
            nums=nums[mid+1:]
        else:
            self.idx+=mid+1
            return self.idx
        
        print(self.idx)
        return self.search(nums, target)

# @lc code=end

