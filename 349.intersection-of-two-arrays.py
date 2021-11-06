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

        stack1,stack2=[],[]
        while nums1:
            queue1=nums1.pop()
            if queue1 not in stack1:
                stack1.append(queue1)
        while stack1:
            queue2=stack1.pop()
            if queue2 in nums2:
                stack2.append(queue2)
        return stack2
# @lc code=end

