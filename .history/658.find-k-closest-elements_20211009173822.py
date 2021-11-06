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

        def bisect(nums, target):
            l, r = 0, len(nums) - 1
            while l+1 < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m
                else:
                    r = m
            return l,r

        l,r = bisect(arr, x)
        length = r-l+1
        if length>k:
            
        elif length<k:

        else:
            return [arr[l], arr[r]]




        


# @lc code=end
# [1,3,5,7,9]\n2\n4

