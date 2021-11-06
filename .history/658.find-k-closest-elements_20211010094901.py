#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return None
        if len(arr)==1 or len(arr)<=k:
            return arr
        if x>=arr[-1]:
            return arr[len(arr)-k+1:]
        if x<=arr[0]:
            return arr[:k]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l+1 < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m
                else:
                    r = m
            return l

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l+1 < r:
                m = (l + r) // 2 
                if nums[m] > target:
                    r = m
                else:
                    l = m
            return r

        l,r = bisect_left(arr, x), bisect_right(arr, x)
        print(l,r)
        if r-l+1>k:
            while r-l+1>k:
                if abs(arr[l+1]-x)>abs(arr[r-1]-x):
                    r=r-1
                else:
                    l=l+1
        if r-l+1<k:
            while r-l+1<k:
                if abs(arr[l-1]-x)>abs(arr[r+1]-x):
                    r=r+1
                else:
                    l=l-1

        return arr[l:r+1]
        


# @lc code=end
# [1,3,5,7,9]\n2\n4

