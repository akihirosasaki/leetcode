#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        while nums1:
            queue1=nums1.pop()
        while stack1:
            queue2=stack1.pop()
            if queue2 in nums2:
                stack2.append(queue2)
        return stack2
# @lc code=end

