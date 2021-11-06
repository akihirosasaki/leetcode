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
        if x>=arr[-1]:
            return arr[len(arr)-k+1:]
        if x<=arr[0]:
            return arr[:k-1]

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

        return [bisect_left(arr, x), bisect_right(arr, x)]

        


# @lc code=end
# [1,3,5,7,9]\n2\n4

