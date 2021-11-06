#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        print(m,n)
        return helper(matrix, target, 10)

        def helper(self, matrix: List[List[int]], target: int, p: int):
            pIndex = find(p, matrix)
            print(pIndex)

# @lc code=end

