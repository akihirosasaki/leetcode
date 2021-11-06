#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if not arr:
#             return None
#         if len(arr)==1 or len(arr)<=k:
#             return arr
#         if x>=arr[-1]:
#             return arr[len(arr)-k:]
#         if x<=arr[0]:
#             return arr[:k]

#         def bisect_left(nums, target):
#             l, r = 0, len(nums) - 1
#             while l+1 < r:
#                 m = (l + r) // 2
#                 if nums[m] < target:
#                     l = m
#                 else:
#                     r = m
#             return l

#         def bisect_right(nums, target):
#             l, r = 0, len(nums) - 1
#             while l+1 < r:
#                 m = (l + r) // 2 
#                 if nums[m] > target:
#                     r = m
#                 else:
#                     l = m
#             return r

#         l,r = bisect_left(arr, x), bisect_right(arr, x)
#         print(l,r)
#         if abs(arr[l]-x)<=abs(arr[r]-x):
#             newl,newr=l,l
#         else:
#             newl,newr=r,r
#         print(newl,newr)
        
#         while (newr-newl+1)<k:
#             if abs(arr[newl-1]-x)<=abs(arr[newr+1]-x) or newr==len(arr)-1:
#                 newl -= 1
#             if abs(arr[newl-1]-x)>abs(arr[newr+1]-x) or newl==0:
#                 newr += 1
        
#         return arr[newl:newr+1]
        

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left)//2

            if x<=arr[mid]:
                right = mid
            elif x >= arr[mid + k]:
                left = mid + 1
            elif x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left+k]

# @lc code=end
# [1,3,5,7,9]\n2\n4

