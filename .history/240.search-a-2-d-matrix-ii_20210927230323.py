#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return None

        m=len(matrix)
        n=len(matrix[0])
        
        if (m,n)==(1,1):
            return matrix[0][0]==target

        midM=m%2
        midN=n%2
        p=matrix[midM][midN]
        
        self.helper(matrix, target, p)
        
    def helper(self, matrix: List[List[int]], target: int, p: int):
        pIndex = self.find(p, matrix)
        print(pIndex)

    def find(element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return (i, j)


        
# @lc code=end

