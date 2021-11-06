#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
"""my answer"""
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low=0
#         high=len(nums)-1
#         while low<=high:
#             mid=(low+high)//2
#             print(low,high,mid)
#             if nums[mid]>target:
#                 if nums[low]<target:
#                     high=mid-1
#                 elif nums[low]>target:
#                     low=mid+1
#                 else:
#                     return low
#             elif nums[mid]<target:
#                 low=mid+1
#                 if nums[low]<target:
#                     high=mid-1
#                 elif nums[low]>target:
#                     low=mid+1
#                 else:
#                     return low
#             else:
#                 return mid

#         return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid

            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return -1




# @lc code=end

