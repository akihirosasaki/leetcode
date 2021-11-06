#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        stack1=[]
        while nums1:
            queue1=nums1.pop()
            if queue1 not in stack1:
                stack1.append(queue1)


# @lc code=end

