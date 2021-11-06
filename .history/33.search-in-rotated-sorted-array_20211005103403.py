#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    idx=0
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums)==0:
        #     return -1
            
        # mid = len(nums)//2
        
        # if nums[mid]>target:
        #     if nums[0]<target:
        #         nums=nums[:mid]
        #     elif nums[0]>target:
        #         self.idx=mid+1
        #         nums=nums[mid+1:]
        #     else:
        #         return self.idx
        # elif nums[mid]<target:
        #     self.idx=mid+1
        #     nums=nums[mid+1:]
        # else:
        #     return self.idx
        
        # print(self.idx)
        # return self.search(nums, target)


        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                if nums[low]<target:
                    high=mid-1
                elif nums[low]>target:
                    low=mid+1
                else:
                    return low
            elif nums[mid]<target:
                low=mid+1
            else:
                return mid

        return -1


# @lc code=end

