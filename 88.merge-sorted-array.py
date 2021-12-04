#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=-1
        while m>0 and n>0:
            if nums1[m-1]<=nums2[n-1]:
                nums1[k]=nums2[n-1]
                n-=1
            else:
                nums1[k]=nums1[m-1]
                nums1[m-1]=0
                m-=1
            k-=1
        if m==0 and n>0:
            nums1[:n]=nums2[:n]

# @lc code=end

