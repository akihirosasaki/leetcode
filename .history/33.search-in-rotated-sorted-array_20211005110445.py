#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            print(low,high,mid)
            if nums[mid]>target:
                if nums[low]<target:
                    high=mid-1
                elif nums[low]>target:
                    low=mid+1
                else:
                    return low
            elif nums[mid]<target:
                low=mid+1
                if nums[low]<target:
                    high=mid-1
                elif nums[low]>target:
                    low=mid+1
                else:
                    return low
            else:
                return mid

        return -1




# @lc code=end

