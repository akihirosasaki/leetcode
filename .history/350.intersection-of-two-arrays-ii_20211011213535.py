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
        
        stack=[]
        while nums1:
            queue=nums1.pop()
            if queue in nums2:
                stack.append(queue)
        return stack
# @lc code=end

